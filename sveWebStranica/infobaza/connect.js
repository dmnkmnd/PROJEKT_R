//pg admin
const { Pool } = require("pg");

const pool = new Pool({
    user: 'grafic',
    host: 'localhost',
    database: 'ProjektRGraf',
    password: '+mentor123+',
    // samo port mjenjate, sve ostalo ostavite isto
    port: 5433,
    idleTimeoutMillis: 300
});

module.exports = pool;