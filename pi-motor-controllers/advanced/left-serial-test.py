import serial
import time

right_wheel = serial.Serial(
        '/dev/ttyUSB1',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
);

left_wheel = serial.Serial(
        '/dev/ttyUSB0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
);

voltage_multiplier = 0.59;
current_multiplier = 3.9;

#time.sleep(1)
##OOoexit;

try:
	print("START");
	hex = serial.to_bytes([0xE1]);
	#left_wheel.write(hex);
	right_wheel.write(hex);
	print("WRITTEN", hex);

	#print("SET DIR RIGHT");
	#hex = serial.to_bytes([0x8A, 0x02]);
	#right_wheel.write(hex);
        #print("WRITTEN", hex);

	#print("SET DIR LEFT");
	#hex = serial.to_bytes([0x8A, 0x01]);
	#left_wheel.write(hex);
	#print("WRITTEN", hex);

	#hex = serial.to_bytes([0x80, 0x7f]);
	#left_wheel.write(hex);
	#hex = serial.to_bytes([0x80, 0x7f]);
	#right_wheel.write(hex);
	#print("WRITTEN", hex);

	#hex = serial.to_bytes([0xCC]);
	#left_wheel.write(hex);
	#print("WRITTEN", hex);

	#time.sleep(10);

        hex = serial.to_bytes([0xCC]);
        right_wheel.write(hex);
        print("WRITTEN", hex);

	while True:
		print("READING LEFT");

		line = right_wheel.read();
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
	left_wheel.close();
	right_wheel.close();
