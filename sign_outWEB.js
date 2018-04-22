var http = require('http');
var url = require('url');
const sqlite3 = require('sqlite3').verbose();


http.createServer(function (req, res) {

// open the database
let db = new sqlite3.Database('/Users/kulnahor/sign_out.db');

let sql = `SELECT * FROM Users`;

db.each(sql, [], (err, row) => {
if (err) {
  throw err;
}
console.log(`${row.id} was at ${row.loc} at ${row.time}`);
});

// close the database connection
db.close();

res.end('Welcome to The SIGN-OUT Webserver!');

}).listen(8080);
