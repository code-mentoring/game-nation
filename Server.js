// This file will be the backend server 
//

const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/test-index.html');
});

io.on('connection', (socket) => {
  console.log('a user connected');
});

http.listen(5000, () => {
  console.log('listening on *:5000');
});
