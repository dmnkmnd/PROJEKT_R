var express = require('express');
var router = express.Router();
const pool = require('../infobaza/connect');

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
router.get('/dijametar', function(req, res, next){
    
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