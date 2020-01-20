# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import serial
import time

ser1 = serial.Serial("/dev/ttySC1",115200,timeout=1)
ser2 = serial.Serial("/dev/ttySC2",115200,timeout=1)
time.sleep(1)
ser.flushInput()

data = ""
while 1: 
    while ser1.inWaiting() > 0:
        data += ser1.read(ser1.inWaiting())
    if data != "":
        for i in range(len(data)):
            print data[i],
        print ""
        data = ""
    while ser2.inWaiting() > 0:
        data += ser1.read(ser2.inWaiting())
    if data != "":
        for i in range(len(data)):
            print data[i],
        print ""
        data = ""
