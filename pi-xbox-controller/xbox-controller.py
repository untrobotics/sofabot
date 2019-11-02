from __future__ import print_function
import xbox
import time

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

print("START");
hex_str = serial.to_bytes([0xE1]);
left_wheel.write(hex_str);
right_wheel.write(hex_str);
print("WRITTEN", str(hex_str));

def show(*args):
    for arg in args:
        print(arg, end="")

joy = xbox.Joystick()

try:
    while not joy.Back():
        right_trigger = joy.rightTrigger()
        speed = int(right_trigger*127)
        hex_speed = hex(speed)
        print("Speed", speed, hex_speed);

        #hex = serial.to_bytes([0x80, 0x00]);
        #left_wheel.write(hex);
        hex_str = serial.to_bytes([0x80, speed]);
        right_wheel.write(hex_str);
        print("WRITTEN", hex_str);

        #####################################

        left_trigger = joy.leftTrigger()
        speed = int(left_trigger*127)
        hex_speed = hex(speed)
        print("Speed", speed, hex_speed);

        #hex = serial.to_bytes([0x80, 0x00]);
        #left_wheel.write(hex);
        hex_str = serial.to_bytes([0x80, speed]);
        left_wheel.write(hex_str);
        print("WRITTEN", hex_str);

finally:
    # Close out when done
    joy.close()
    left_wheel.close();
    right_wheel.close();
