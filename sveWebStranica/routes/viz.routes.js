var express = require('express');
var router = express.Router();
const pool = require('../infobaza/connect');
const { spawn } = require('child_process');
const path = require('path');

// Closeness Centrality
router.get('/closenessCentrality', function(req, res, next){
    // zamjeni nesto kao naziv view-a
    res.render('nesto', { 
        
    });
});

// Betweenness centrality
router.get('/betweennessCentrality', function(req, res, next){
    
});

// Tarjanov algoritam
router.get('/TarjanovAlgoritam', function(req, res, next){
    
});

// Adamec-Adar indeks
router.get('/AdamecAdarIndex', function(req, res, next){
    
});

// dijametar
router.get('/dijametar', function (req, res, next) {
    res.render('dijkstra', { graf: req.session.graf });
});
router.get('/dijametarPodaci', function (req, res, next) {
    const cvorA = req.query.cvorA;
    const cvorB = req.query.cvorB;
    const preskakanje = req.query.preskakanje;

    const pythonScriptPath = path.join(__dirname, '../public/scripts/dijkstra/main.py');
    const graf = JSON.stringify(req.session.graf);
    const pythonProcess = spawn('python', [pythonScriptPath, graf, cvorA, cvorB, preskakanje]);
    pythonProcess.on('close', (code) => {
        if (code === 0) {
            res.send({ message: 'Python skripta uspješno izvršena.'});
        } else {
            res.status(500).send({ message: 'Greška pri izvršavanju Python skripte.', code });
        }
    });
});


// HITS algoritam
router.get('/HITSAlgoritam', function(req, res, next){
    
});

// PageRank
router.get('/PageRankAlgoritam', function(req, res, next){
    
});

// Louvain Method
router.get('/LouvainMetoda', function(req, res, next){
    
});

// Girvan-Newman Algoritam
router.get('/GirvanNewmanAlgoritam', function(req, res, next){
    
});

module.exports = router;