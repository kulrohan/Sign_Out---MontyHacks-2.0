var http = require('http');
var url = require('url');
var fs = require('fs');

http.createServer(function (req, res) {

var q = url.parse(req.url, true).query;


const sqlite3 = require('sqlite3').verbose();

let db = new sqlite3.Database('/Users/kulnahor/sign_out.db');

let sql = 'SELECT * FROM Users WHERE id = 103488 AND entry_num = (SELECT MAX(Entry) FROM Family)';


var input = q.name;
db.get(sql, [], (err, rows) => {
  if (err) {
    throw err;
  };
  return rows ? console.log(rows.loc)
  : console.log(`No playlist found with the id ${playlistId}`);
  res.end()

  res.writeHead(200, {'Content-Type': 'text/plain'});

  res.write('<p>hi</p>');
  //res.write(input + " was at " + rows.Location + " at " + rows.Time);
});
//res.write();
res.end('Welcome to The SIGN-OUT Webserver!');

}).listen(8080); //the server object listens on port 8080




//create a server object:

   //end the response






 //(err) => {
//if (err) {
//  console.error(err.message);
//}
