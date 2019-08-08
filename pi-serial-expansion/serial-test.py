import serial
import time

ser = serial.Serial(
	'/dev/ttySC1',
	baudrate = 9600,
	parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
);

time.sleep(1)

try:
	print("START");
	hex = serial.to_bytes([0xE1]);
	ser.write(hex);
	print("WRITTEN", hex);

	hex = serial.to_bytes([0x80, 0x00]);
	ser.write(hex);
	print("WRITTEN", hex);

	hex = serial.to_bytes([0xCC]);
	ser.write(hex);
	print("WRITTEN", hex);

	#while True:
	#	print("READING");
	#	line = ser.read();
	#	print(["DATA: '", line, "'"]);

finally:
	ser.close();
