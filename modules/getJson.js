module.exports.jsonGetquery = async () => {
    const mysql = require("mysql")
    const connection = mysql.createConnection({
        host: "localhost",
        user: "root",
        password: "sjml0724@@",
        database: "gpsservice"
    });
    connection.connect();

    return new Promise((resolve, reject) => {
        connection.query("select * from location", (err, result) => {
            if (err) reject(err)
            else resolve(result)
        });
    });
}
