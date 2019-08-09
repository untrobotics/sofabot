import serial
import time

ser = serial.Serial(
	'/dev/ttySC0',
	baudrate = 9600,
	parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
);

ser2 = serial.Serial(
        '/dev/ttyUSB0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
);

voltage_multiplier = 0.59;
current_multiplier = 3.9;

time.sleep(1)

try:
	print("START");
	hex = serial.to_bytes([0xE1]);
	ser.write(hex);
	print("WRITTEN", hex);

	hex = serial.to_bytes([0x80, 0x12]);
	ser.write(hex);
	print("WRITTEN", hex);

	hex = serial.to_bytes([0xCC]);
	ser.write(hex);
	print("WRITTEN", hex);

	time.sleep(1);

	while True:
		print("READING");
		line = ser2.read();
		hex_value = line.encode("hex");
		integer_value = int(line.encode("hex"), 16);

		if (integer_value == 255): # End of command
			break;

		print(["DATA: ", "0x" + hex_value, integer_value]);

		voltage = integer_value * voltage_multiplier;
		print("VOLTAGE:", voltage, "V");

#	hex = serial.to_bytes([0xCA]);
#	ser.write(hex);
#	print("WRITTEN", hex);
#
#	time.sleep(1)
#
#	while True:
#		print("READING");
#		line = ser2.read();
#		hex_value = line.encode("hex");
#		integer_value = int(line.encode("hex"), 16);
#
#		if (integer_value == 255): # End of command
#			break;
#
#		print(["DATA: ", "0x" + hex_value, integer_value]);
#
#		current = integer_value * current_multiplier;
#		print("CURRENT:", current, "A");

finally:
	ser.close();
