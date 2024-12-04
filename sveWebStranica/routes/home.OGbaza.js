var express = require('express');
var router = express.Router();
const pool = require('../infobaza/connect');

// kod vezan za čitanje iz txt
const multer = require('multer');
const fs = require('fs');
const path = require('path');
const readline = require('readline');
const { time, log } = require('console');

// Konfiguracija za multer
const upload = multer({ dest: 'uploads/' });

// home stranica
router.get('/', async(req, res, next) => {
    if(req.session.graf != undefined){
        res.render('proba', {
            graf: JSON.stringify(req.session.graf)
        });

    } else {
        res.render('home', {
            
        });
    }

    
});

router.post('/add/txt', upload.single('file'), async (req, res, next) => {
    const file = req.file;

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

        // Obrada linija i spremanje grafa
        const d = new Date();
        let idgraf = d.getTime() % 10000000;
        const graf = {};

        try {
            const client = await pool.connect();

            try {
                // Ubacivanje grafa u bazu
                const result = await client.query('INSERT INTO graf (email) VALUES ($1) RETURNING idgraf', [idgraf]);
                idgraf = result.rows[0].idgraf;
                req.session.idgraf = idgraf;

                // Obrada linija u `for...of` petlji
                for (const linija of lines) {
                    const nazivvrh = linija.split(";")[0];

                    // Dodavanje vrha u graf
                    graf[nazivvrh] = [];

                    // Provjera i dodavanje vrha u bazu
                    let idvrh1 = await client.query('SELECT idVrh FROM vrh WHERE nazivvrh=$1 and idgraf=$2', [nazivvrh, idgraf]);
                    if (idvrh1.rows.length === 0) {
                        idvrh1 = await client.query('INSERT INTO vrh (nazivvrh, idgraf) VALUES ($1, $2) RETURNING idVrh', [nazivvrh, idgraf]);
                    }
                    idvrh1 = idvrh1.rows[0].idvrh;

                    // Iteracija kroz susjede
                    const susjedi = linija.split(";")[1].split(",");
                    for (const susjed of susjedi) {
                        let idvrh2 = await client.query('SELECT idVrh FROM vrh WHERE nazivvrh=$1 and idgraf=$2', [susjed, idgraf]);
                        if (idvrh2.rows.length === 0) {
                            idvrh2 = await client.query('INSERT INTO vrh (nazivvrh, idgraf) VALUES ($1, $2) RETURNING idVrh', [susjed, idgraf]);
                        }
                        idvrh2 = idvrh2.rows[0].idvrh;

                        // Dodavanje susjeda u graf
                        graf[nazivvrh].push(susjed);

                        // Dodavanje veze u bazu
                        await client.query('INSERT INTO jeSusjed (idvrh1, idvrh2) VALUES ($1, $2);', [idvrh1, idvrh2]);
                    }
                }
            } finally {
                client.release(); // Vraća konekciju nazad u pool
            }
        } catch (err) {
            console.error('Greška u bazi podataka:', err);
            return res.status(500).send('Greška u bazi podataka.');
        }

        // Graf spremljen u JSON
        req.session.graf = graf;
        res.redirect('/');

    } catch (err) {
        console.error('Greška pri obradi dokumenta:', err);
        return res.status(500).send('Greška pri obradi dokumenta.');
    }
});

router.post('/add/json', upload.single('file'), async (req, res) => {
    const file = req.file;

    if (!file) {
        return res.status(400).send('Nije uploadan niti jedan JSON dokument.');
    }

    const filePath = path.join(__dirname, '../', file.path);

    try {
        const fileData = await fs.promises.readFile(filePath, 'utf8');
        const graf = JSON.parse(fileData); 

        // spremanje u bazu 
        for (const kljuc in graf) {
            for (const elem of graf[kljuc]) { 
                console.log(kljuc + ' : ' + elem);
            }
        }

        await fs.promises.unlink(filePath);

        // Graf spremljen u JSON
        req.session.graf = graf;
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



/*
SELECT * FROM vrh 
	JOIN jesusjed on idvrh1=idvrh 
		JOIN vrh AS vrh2 ON idvrh2=vrh2.idvrh 
		WHERE vrh.idgraf=27
		ORDER BY vrh.nazivVrh
*/


module.exports = router;
