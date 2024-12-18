const express = require('express');

const app = express();
const path = require('path');

const session = require("express-session");

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(express.static(path.join(__dirname, 'public')));

app.use(express.urlencoded({
    extended: true
}));

// moj kod 
app.use('/styles', express.static(__dirname + '/public/css'));
app.use('/slike', express.static(__dirname + 'public/slike'));

app.use(session({
    secret: 'FER WiM', 
    resave: false, 
    saveUninitialized: true, 
   }))

const homeRouter = require('./routes/home.routes');
app.use('/', homeRouter);

const vizRouter = require('./routes/viz.routes');
app.use('/viz', vizRouter);
// kraj 

const PORT = 8080;
app.listen(PORT, () => {
    console.log(`Listening on port ${PORT}!`);
})