var express = require('express');
var router = express.Router();
const pool = require('../infobaza/connect');

// kod vezan za čitanje iz txt
const multer = require('multer');
const fs = require('fs');
const path = require('path');
const readline = require('readline');
//const { time, log } = require('console');

// kdo vezan uz pozivanje pythona
const { exec } = require('child_process');

// Konfiguracija za multer
const upload = multer({ dest: 'uploads/' });

// home stranica
router.get('/', async(req, res, next) => {
    if(req.session.graf != undefined){

        // za prikaz grafova u bazi
        try {
            const client = await pool.connect();

            try {
                var uneseni = await client.query('SELECT * FROM baza');
                uneseni = uneseni.rows;

            } finally {
                client.release(); 
            }
        } catch (err) {
            console.error('Greška u bazi podataka:', err);
            return res.status(500).send('Greška u bazi podataka.');
        }

        // za stavranje slike grafa koji je odabran
        const jsonData = JSON.stringify(req.session.graf); 
        const outputImagePath = path.join(__dirname.toString(), '../public/slike', 'graf.png');  

        const pythonScriptPath = path.join(__dirname, '../public/scripts/v_obcni.py');

        const command = `python "${pythonScriptPath}" "${outputImagePath}"`;

        const pythonProcess = exec(command);

        pythonProcess.stdin.write(jsonData);
        pythonProcess.stdin.end();

        pythonProcess.stdout.on('data', (data) => {
            console.log(data.toString());
        });

        pythonProcess.stderr.on('data', (data) => {
            console.error(`stderr: ${data}`);
        });

        pythonProcess.on('close', (code) => {
            if (code === 0) {
                // Nakon što je Python skripta završila, šaljemo sliku kao putanju
                res.render('home', {
                    graf: "/slike/graf.png",  // Putanja slike koja je generirana
                    ime: req.session.ime, 
                    prikazi: JSON.stringify(uneseni)
                });
            } else {
                console.error('Greška pri generiranju grafa.');
                res.status(500).send('Greška pri generiranju grafa.');
            }
        });


    } else {

        try {
            const client = await pool.connect();

            try {
                var uneseni = await client.query('SELECT * FROM baza');
                uneseni = uneseni.rows;

            } finally {
                client.release(); 
            }
        } catch (err) {
            console.error('Greška u bazi podataka:', err);
            return res.status(500).send('Greška u bazi podataka.');
        }

        res.render('home', {
            graf: undefined,
            ime: undefined, 
            prikazi: JSON.stringify(uneseni)
        });
    }

    
});

// promjena grafa koje se obrađuje
router.post('/noviodobir', upload.single('file'), async (req, res, next) => {
    req.session.graf = undefined;
    req.session.ime = undefined;
    res.redirect('/');
});

// promjena grafa koje se obrađuje
router.get('/noviodobir', upload.single('file'), async (req, res, next) => {
    req.session.graf = undefined;
    req.session.ime = undefined;
    res.redirect('/');
});

// odbir već unesenog grafa 
router.post('/stariodobir', upload.single('file'), async (req, res, next) => {
    var uneseni;
    try {
        const client = await pool.connect();

        try {
            uneseni = await client.query('SELECT * FROM baza WHERE id = $1', [req.body.grafid]);

        } finally {
            client.release(); 
        }
    } catch (err) {
        console.error('Greška u bazi podataka:', err);
        return res.status(500).send('Greška u bazi podataka.');
    }

    uneseni = uneseni.rows[0];

    req.session.graf = uneseni.data;
    req.session.ime = uneseni.ime;

    res.redirect('/');
});

// dodavnje novog grafa kroz .txt
router.post('/add/txt', upload.single('file'), async (req, res, next) => {
    const file = req.file;
    const ime = req.body.nazivGrafa;

    if (!file) {
        return res.status(400).send('Nije uploadan niti jedan dokument.');
    }

    const filePath = path.join(__dirname, '../', file.path);

    try {
        const rl = readline.createInterface({
            input: fs.createReadStream(filePath),
            terminal: false
        });

        // Spremanje linija u polje
        const lines = [];

        rl.on('line', (line) => {
            lines.push(line);
        });

        // Čekanje zatvaranja fajla i njegovog brisanja
        await new Promise((resolve, reject) => {
            rl.on('close', () => {
                fs.unlink(filePath, (err) => {
                    if (err) {
                        console.error('Greška pri brisanju dokumenta:', err);
                        reject(new Error('Greška pri brisanju dokumenta.'));
                    } else {
                        resolve();
                    }
                });
            });
        });

        const graf = {};

        try {
            const client = await pool.connect();

            try {

                // Obrada linija
                for (const linija of lines) {
                    const nazivvrh = linija.split(";")[0];

                    // Dodavanje vrha u graf
                    graf[nazivvrh] = [];

                    // Iteracija kroz susjede
                    const susjedi = linija.split(";")[1].split(",");
                    for (const susjed of susjedi) {
                        if(susjed != ""){ // ako je slucajno prazan skup iza : kraj da ne bi stavrao probleme
                            graf[nazivvrh].push(susjed);
                        }
                    }  
                }

                // Dodavanje grafa u bazu
                await client.query('INSERT INTO baza (data, ime) VALUES ($1, $2)', [graf, ime]);
            } finally {
                client.release(); 
            }
        } catch (err) {
            console.error('Greška u bazi podataka:', err);
            return res.status(500).send('Greška u bazi podataka.');
        }

        // Graf spremljen u JSON
        req.session.graf = graf;
        req.session.ime = ime;
        res.redirect('/');

    } catch (err) {
        console.error('Greška pri obradi dokumenta:', err);
        return res.status(500).send('Greška pri obradi dokumenta.');
    }
});

// dodavnje novog grafa kroz .json
router.post('/add/json', upload.single('file'), async (req, res) => {
    const file = req.file;
    const ime = req.body.nazivGrafa;

    if (!file) {
        return res.status(400).send('Nije uploadan niti jedan JSON dokument.');
    }

    const filePath = path.join(__dirname, '../', file.path);

    try {
        const fileData = await fs.promises.readFile(filePath, 'utf8');
        const graf = JSON.parse(fileData); 

        // Dodavanje grafa u bazu
        try {
            const client = await pool.connect();

            try {

                await client.query('INSERT INTO baza (data, ime) VALUES ($1, $2)', [graf, ime]);

            } finally {
                client.release(); 
            }
        } catch (err) {
            console.error('Greška u bazi podataka:', err);
            return res.status(500).send('Greška u bazi podataka.');
        }


        await fs.promises.unlink(filePath);

        // Graf spremljen u JSON
        req.session.graf = graf;
        req.session.ime = ime;
        res.redirect('/');

    } catch (error) {
        console.error('Greška pri obradi JSON dokumenta.', error);

        // Brisanje u slučaju greške
        try {
            await fs.promises.unlink(filePath);
            console.log('JSON dokument obrisan nakon greške.');
        } catch (unlinkError) {
            console.error('Greška pri brisanju JSON dokumenta.', unlinkError);
        }

        res.status(500).send('Greška pri obradi JSON-a.');
    }
});

module.exports = router;
