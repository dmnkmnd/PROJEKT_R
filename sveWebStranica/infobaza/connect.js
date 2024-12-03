//pg admin
const { Pool } = require("pg");

const pool = new Pool({
    user: 'projektr',
    host: 'localhost',
    database: 'grafProjektR',
    password: '+mentor123+',
    // samo port mjenjate, sve ostalo ostavite isto
    port: 5433,
    idleTimeoutMillis: 300
});

module.exports = pool;