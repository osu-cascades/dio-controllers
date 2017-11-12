var serialport = require("serialport");
var readline = require("readline");
var SerialPort = serialport;

var sp = new SerialPort("/dev/cu.usbmodem1451", {
	baudrate:9600,
	databits: 8,
	parity: 'none',
	stopBits: 1,
	flowControl: false,
	parser: serialport.parsers.readline("\r\n"),
});

sp.on('open', function() {
   console.log('open');
   sp.on('data', function(data) {
      console.log('data received: ' + data);
   });
});