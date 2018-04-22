var http = require('http');

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    var txt = "Hello World!";
    console.log(console.log());
    res.end(txt);
}).listen(8080);
