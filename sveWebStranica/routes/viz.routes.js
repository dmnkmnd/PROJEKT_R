var express = require('express');
var router = express.Router();
const pool = require('../infobaza/connect');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');
const fsPromise = require('fs').promises;

router.get('/obrisiSlike', async (req, res) => {
    const direktorijSlika = 'public/slike';
    const regex = /^slika\d+\.png$/;

    try {
        const files = await fsPromise.readdir(direktorijSlika);
        const slikeZaBrisanje = files.filter(file => regex.test(file));
        if (slikeZaBrisanje.length === 0)
            return res.json({ message: "Nema slika za brisanje." });
        for (const file of slikeZaBrisanje) {
            const filePath = path.join(direktorijSlika, file);
            await fsPromise.unlink(filePath);
        }
        res.json({ message: "Slike su uspješno izbrisane." });
    } catch (err) {
        console.error("Greška pri čitanju direktorija ili brisanju slika:", err);
        res.status(500).json({ message: "Greška pri čitanju direktorija ili brisanju slika." });
    }
});


// Closeness Centrality
router.get('/closenessCentrality', function(req, res, next){
    res.render('closenessCentrality', { graf: req.session.graf });
});
router.get('/closenessCentralityPodaci', function (req, res) {
    const pythonScriptPath = path.join(__dirname, '../public/scripts/closenessCentrality/main.py');
    const graf = JSON.stringify(req.session.graf);
    const pythonProcess = spawn('python', [pythonScriptPath, graf]);
    pythonProcess.on('close', (code) => {
        if (code === 0) {
            fs.readdir('public/slike', (err, files) => {
                if (err) {
                    console.error(err);
                    res.status(500).send({ message: 'Greška pri dohvaćanju slika.' });
                } else {
                    const brSlika = files.filter(file => /^slika\d+\.png$/.test(file)).length;
                    res.json({ brSlika });
                }
            });
        } else {
            res.status(500).send({ message: 'Greška pri izvršavanju Python skripte.', code });
        }
    });
});

// Betweenness centrality
router.get('/betweennessCentrality', function(req, res, next){
    res.render('betweennessCentrality', { graf: req.session.graf });
});
router.get('/betweennessCentralityPodaci', function (req, res) {
    const pythonScriptPath = path.join(__dirname, '../public/scripts/betweennessCentrality/main.py');
    const graf = JSON.stringify(req.session.graf);
    const pythonProcess = spawn('python', [pythonScriptPath, graf]);
    pythonProcess.on('close', (code) => {
        if (code === 0) {
            fs.readdir('public/slike', (err, files) => {
                if (err) {
                    console.error(err);
                    res.status(500).send({ message: 'Greška pri dohvaćanju slika.' });
                } else {
                    const brSlika = files.filter(file => /^slika\d+\.png$/.test(file)).length;
                    res.json({ brSlika });
                }
            });
        } else {
            res.status(500).send({ message: 'Greška pri izvršavanju Python skripte.', code });
        }
    });
});

// Tarjanov algoritam
router.get('/TarjanovAlgoritam', function(req, res, next){
    res.render('tarjan', { graf: req.session.graf });
});
router.get('/TarjanovAlgoritamPodaci', function(req, res, next){
    const pythonScriptPath = path.join(__dirname, '../public/scripts/tarjan/main.py');
    const graf = JSON.stringify(req.session.graf);
    const pythonProcess = spawn('python', [pythonScriptPath, graf]);
    pythonProcess.on('close', (code) => {
        if (code === 0) {
            fs.readdir('public/slike', (err, files) => {
                if (err) {
                    console.error(err);
                    res.status(500).send({ message: 'Greška pri dohvaćanju slika.' });
                } else {
                    const brSlika = files.filter(file => /^slika\d+\.png$/.test(file)).length;
                    res.json({ brSlika });
                }
            });
        } else {
            res.status(500).send({ message: 'Greška pri izvršavanju Python skripte.', code });
        }
    });
});

// Adamec-Adar indeks
router.get('/AdamecAdarIndex', function(req, res, next){
    res.render('adamicAdar', { graf: req.session.graf });
});
router.get('/AdamecAdarIndexPodaci', function(req, res){
    const cvorA = req.query.cvorA;
    const cvorB = req.query.cvorB;
    const pythonScriptPath = path.join(__dirname, '../public/scripts/adamicAdar/main.py');
    const graf = JSON.stringify(req.session.graf);
    const pythonProcess = spawn('python', [pythonScriptPath, graf, cvorA, cvorB]);
    pythonProcess.on('close', (code) => {
        if (code === 0) {
            fs.readdir('public/slike', (err, files) => {
                if (err) {
                    console.error(err);
                    res.status(500).send({ message: 'Greška pri dohvaćanju slika.' });
                } else {
                    const brSlika = files.filter(file => /^slika\d+\.png$/.test(file)).length;
                    res.json({ brSlika });
                }
            });
        } else {
            res.status(500).send({ message: 'Greška pri izvršavanju Python skripte.', code });
        }
    });
});

// dijametar
router.get('/dijametar', function (req, res, next) {
    res.render('dijkstra', { graf: req.session.graf });
});
router.get('/dijametarPodaci', function (req, res) {
    const cvorA = req.query.cvorA;
    const cvorB = req.query.cvorB;
    const preskakanje = req.query.preskakanje;
    const pythonScriptPath = path.join(__dirname, '../public/scripts/dijkstra/main.py');
    const graf = JSON.stringify(req.session.graf);
    const pythonProcess = spawn('python', [pythonScriptPath, graf, cvorA, cvorB, preskakanje]);
    pythonProcess.on('close', (code) => {
        if (code === 0) {
            fs.readdir('public/slike', (err, files) => {
                if (err) {
                    console.error(err);
                    res.status(500).send({ message: 'Greška pri dohvaćanju slika.' });
                } else {
                    const brSlika = files.filter(file => /^slika\d+\.png$/.test(file)).length;
                    res.json({ brSlika });
                }
            });
        } else {
            res.status(500).send({ message: 'Greška pri izvršavanju Python skripte.', code });
        }
    });
});


// HITS algoritam
router.get('/HITSAlgoritam', function(req, res, next){
    res.render('hits', { graf: req.session.graf });
});
router.get('/HITSAlgoritamPodaci', function(req, res, next){
    const iteracija = req.query.iteracija;
    const pythonScriptPath = path.join(__dirname, '../public/scripts/hits/main.py');
    const graf = JSON.stringify(req.session.graf);
    const pythonProcess = spawn('python', [pythonScriptPath, graf, iteracija]);
    pythonProcess.on('close', (code) => {
        if (code === 0) {
            fs.readdir('public/slike', (err, files) => {
                if (err) {
                    console.error(err);
                    res.status(500).send({ message: 'Greška pri dohvaćanju slika.' });
                } else {
                    const brSlika = files.filter(file => /^slika\d+\.png$/.test(file)).length;
                    res.json({ brSlika });
                }
            });
        } else {
            res.status(500).send({ message: 'Greška pri izvršavanju Python skripte.', code });
        }
    });
});

// PageRank
router.get('/PageRankAlgoritam', function(req, res, next){
    res.render('pageRank', { graf: req.session.graf });
});
router.get('/PageRankAlgoritamPodaci', function(req, res, next){
    const preskakanje = req.query.preskakanje;
    const pythonScriptPath = path.join(__dirname, '../public/scripts/pageRank/main.py');
    const graf = JSON.stringify(req.session.graf);
    const pythonProcess = spawn('python', [pythonScriptPath, graf, preskakanje]);
    pythonProcess.on('close', (code) => {
        if (code === 0) {
            fs.readdir('public/slike', (err, files) => {
                if (err) {
                    console.error(err);
                    res.status(500).send({ message: 'Greška pri dohvaćanju slika.' });
                } else {
                    const brSlika = files.filter(file => /^slika\d+\.png$/.test(file)).length;
                    res.json({ brSlika });
                }
            });
        } else {
            res.status(500).send({ message: 'Greška pri izvršavanju Python skripte.', code });
        }
    });
});

// Louvain Method
router.get('/LouvainMetoda', function(req, res, next){
    res.render('louvain', { graf: req.session.graf });
});
router.get('/LouvainMetodaPodaci', function(req, res, next){
    const pythonScriptPath = path.join(__dirname, '../public/scripts/louvain/main.py');
    const graf = JSON.stringify(req.session.graf);
    const pythonProcess = spawn('python', [pythonScriptPath, graf]);
    pythonProcess.on('close', (code) => {
        if (code === 0) {
            fs.readdir('public/slike', (err, files) => {
                if (err) {
                    console.error(err);
                    res.status(500).send({ message: 'Greška pri dohvaćanju slika.' });
                } else {
                    const brSlika = files.filter(file => /^slika\d+\.png$/.test(file)).length;
                    res.json({ brSlika });
                }
            });
        } else {
            res.status(500).send({ message: 'Greška pri izvršavanju Python skripte.', code });
        }
    });
});

// Girvan-Newman Algoritam
router.get('/GirvanNewmanAlgoritam', function(req, res, next){
    res.render('girvanNewman', { graf: req.session.graf });
});
router.get('/girvanNewmanPodaci', function (req, res) {
    const brZajednica = req.query.brZajednica;
    const preskakanje = req.query.preskakanje;
    const pythonScriptPath = path.join(__dirname, '../public/scripts/girvanNewman/main.py');
    const graf = JSON.stringify(req.session.graf);
    const pythonProcess = spawn('python', [pythonScriptPath, graf, brZajednica, preskakanje]);
    pythonProcess.on('close', (code) => {
        if (code === 0) {
            fs.readdir('public/slike', (err, files) => {
                if (err) {
                    console.error(err);
                    res.status(500).send({ message: 'Greška pri dohvaćanju slika.' });
                } else {
                    const brSlika = files.filter(file => /^slika\d+\.png$/.test(file)).length;
                    res.json({ brSlika });
                }
            });
        } else {
            res.status(500).send({ message: 'Greška pri izvršavanju Python skripte.', code });
        }
    });
});

module.exports = router;