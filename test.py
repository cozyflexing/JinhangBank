import serial
import time

ser = serial.Serial("/dev/serial0", 9600)  # open the serial port at 9600 baud

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode("utf-8").rstrip()  # read a '\n' terminated line
        print(line)
    time.sleep(0.1)
