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
hex = serial.to_bytes([0xE1]);
left_wheel.write(hex);
right_wheel.write(hex);
print("WRITTEN", hex);

def show(*args):
    for arg in args:
        print(arg, end="")

joy = xbox.Joystick()

try:
    while not joy.Back():
        # Show connection status
    #show("Connected:")
    #showIf(joy.connected(), "Y", "N")
    # Left analog stick
    #show("  Left X/Y:", fmtFloat(joy.leftX()), "/", fmtFloat(joy.leftY()))
    # Right trigger

    show("  RightTrg:", fmtFloat(joy.rightTrigger()), "\n")
    right_trigger = joy.rightTrigger()
    speed = int(right_trigger*127)
    hex_speed = hex(speed)
    print("Speed", speed, hex_speed);

    # A/B/X/Y buttons
    #show("  Buttons:")
    #showIf(joy.A(), "A")
    #showIf(joy.B(), "B")
    #showIf(joy.X(), "X")
    #showIf(joy.Y(), "Y")
    # Dpad U/D/L/R
    #show("  Dpad:")
    #showIf(joy.dpadUp(),    "U")
    #showIf(joy.dpadDown(),  "D")
    #showIf(joy.dpadLeft(),  "L")
    #showIf(joy.dpadRight(), "R")
    # Move cursor back to start of line
    #show(chr(13))

# Close out when done
joy.close()
