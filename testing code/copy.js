var http = require('http');
var url = require('url');
var fs = require('fs');


//var q = url.parse(req.url, true).query;


const sqlite3 = require('sqlite3').verbose();

let db = new sqlite3.Database('/Users/kulnahor/test.db');

let sql = 'SELECT * FROM Family WHERE Name = "Rohan" AND  Entry = (SELECT MAX(Entry) FROM Family)';


//var input = q.name;
db.get(sql, [], (err, rows) => {
  if (err) {
    throw err;
  };
  http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  return rows ? res.write('hi')
  : console.log(`No playlist found with the id ${playlistId}`);
  res.end();


  //res.write(input + " was at " + rows.Location + " at " + rows.Time);
}).listen(8080);
//res.write();
//res.end('hiadkfasdkjfh');

}); //the server object listens on port 8080




//create a server object:

   //end the response






 //(err) => {
//if (err) {
//  console.error(err.message);
//}
