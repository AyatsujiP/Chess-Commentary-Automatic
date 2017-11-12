var id = 0;
const http = require('http');
var stockfish = require('stockfish');
var stockfishes = [];
var msg = "";

stockfishes[id] = stockfish();

stockfishes[id].onmessage = function(message){
  console.log("Message get: " + message);
  msg += message;
}

stockfishes[id].postMessage('ucinewgame');
stockfishes[id].postMessage('isready');
//stockfishes[id].postMessage('setoption name UCI_AnalyseMode value true');
stockfishes[id].postMessage('position startpos moves e2e4 c7c5');
stockfishes[id].postMessage('go depth 10');
stockfishes[id].postMessage('stop');

const PORT = 8008;

http.createServer((request, response ) =>{
  response.writeHead(200,{'Content-Type': 'text/plain'});
  response.end(msg);
}).listen(PORT);

console.log('Server Running......');
