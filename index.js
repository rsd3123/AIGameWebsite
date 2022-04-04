/****
 * Tic-Tac-Toe Website Server
 * Rudy DeSanti
 * March 31, 2022
 */

const express = require('express');
const { range } = require('express/lib/request');
const app = express();
const http = require('http');

const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);

const {PythonShell} =require('python-shell');

//let shell = new PythonShell('tttSearchAgent.py', {mode: 'text'})

/*Give HTML to client*/
app.use(express.static('public'));
app.get('/', async(req, res) => {
  //res.sendFile(__dirname + '/tictactoe.css');
  res.sendFile(__dirname + '/public/tictactoe.html');
  
});


/*When socket is connected*/
io.on('connection', (socket) => {
  console.log('a user connected');
  var id = socket.id;
  
  socket.on('message', (message) => {
    message = JSON.parse(message);

    switch(message.type)
    {
        case "AITurn":
            {
                console.log(message.type);
                console.log(message.gamestate);
                console.log(message.diff);
                //Python make AI move
                let options = {
                    mode: 'text',
                    pythonOptions: ['-u'], // get print results in real-time
                    args: [message.gamestate, message.diff] //An argument which can be accessed in the script using sys.argv[1]
                };
                PythonShell.run('tttSearchAgent.py', options, function (err, result){
                    if (err) throw err;
                    // result is an array consisting of messages collected
                    //during execution of script.
                    console.log('result: ', result.toString());
                    var answer = JSON.stringify({type: 'AITurn', square:result});
                    io.to(id).emit('message', answer);
                });
            }
            break;
        }
    });
  socket.on('disconnect', () => {
    console.log('user disconnected');
  });
});

server.listen(3000, '0.0.0.0', () => {
  console.log('listening on *:3000');
});

