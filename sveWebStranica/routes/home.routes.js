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
            graf: req.session.graf
        });

    } else {
        res.render('home', {
            
        });
    }

    
});

// dodoavnaje novog grafa u sustav 
router.post('/add', upload.single('file'), async (req, res, next) => {
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

        // Privremena kolekcija za redove
        const lines = [];

        rl.on('line', (line) => {
            lines.push(line); 
        });

        // brisanje dokumenta
        rl.on('close', () => {

            req.session.graf = lines;

            // Brisanje fajla
            fs.unlink(filePath, (err) => {
                if (err) {
                    console.error('Greška pri brisanju dokumenta:', err);
                    return res.status(500).send('Greška pri brisanju dokumenta.');
                }
            });
        });

        // obrada linije 
        var d = new Date();
        var idgraf = d.getTime()%10000000;

        try {
            const client = await pool.connect();
            
            try {

                // ubacivanje grafa u bazu
                idgraf = await client.query('INSERT INTO graf (email) VALUES ($1) RETURNING idgraf', [idgraf]); 
                idgraf = idgraf.rows[0].idgraf;

                // ubacivanje vrhova i bridova u bazu
                lines.forEach(async function(linija) {
                    var nazivvrh = linija.split(";")[0];

                    // provjera je li cvor vec dodan 
                    var idvrh1 = await client.query('SELECT idVrh FROM vrh WHERE nazivvrh=$1 and idgraf=$2', [nazivvrh, idgraf]);
            
                    if (idvrh1.rows.length == 0) {
                        idvrh1 = await client.query('INSERT INTO vrh (nazivvrh, idgraf) VALUES ($1,$2) RETURNING idVrh', [nazivvrh, idgraf]);
                    }
                    idvrh1 = idvrh1.rows[0].idvrh;

                    linija.split(";")[1].split(",").forEach( async function(susjed){
                        // provjera je li cvor vec dodan 
                        var idvrh2 = await client.query('SELECT idVrh FROM vrh WHERE nazivvrh=$1 and idgraf=$2', [susjed, idgraf]);
            
                        if (idvrh2.rows.length == 0) {
                            idvrh2 = await client.query('INSERT INTO vrh (nazivvrh, idgraf) VALUES ($1,$2) RETURNING idVrh', [susjed, idgraf]);
                        }
                        idvrh2 = idvrh2.rows[0].idvrh;


                        await client.query('INSERT INTO jeSusjed (idvrh1, idvrh2) VALUES ($1, $2);', [idvrh1, idvrh2]);
                    });
            
                });
            } finally {
                client.release();  // Vraća konekciju nazad u pool
            }
        } catch (err) {
            console.error(err);
            res.status(500).send("Greška u bazi podataka.");
        }

        res.redirect('/');

    } catch (err) {
        console.error('Greška:', err);
        return res.status(500).send('Greška pri obradi dokumenta.');
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

/*
try {
        const client = await pool.connect();
        
        try {
            const result = await client.query('SELECT * FROM vrh NATURAL JOIN graf WHERE idgraf = $1', [1]);
            
            if (result.rows.length > 0) {
                pass = result.rows[0].nazivvrh;
            } else {
                console.log("Email nije pronađen.");
            }
        } finally {
            client.release();  // Vraća konekciju nazad u pool
        }
    } catch (err) {
        console.error(err);
        res.status(500).send("Greška u bazi podataka.");
    }
*/