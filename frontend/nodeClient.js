var net = require('net');

var client = new net.Socket();
client.connect(5050, '10.0.0.5', function() {
    console.log('Connected');
    client.write('yes');
});
client.on('data', function(data) {
    console.log('Received: ' + data);
    client.destroy(); // kill client after server's response
});