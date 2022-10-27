//node C:\Users\c0523140\Desktop\WORK\ALL\nodejs.js

var http = require('http');
var url = require('url');

var server = http.createServer((req, res) =>{
   var q = url.parse(req.url, true).query;
   var txt = q.name + " " + q.password;
   res.writeHead(200, {'Content-Type': 'text/html'});
   res.write(txt);
   res.end();
});

server.listen(8080);