# views/arduinoInput.py
import serial

ser = serial.Serial("/dev/serial0", 9600)

while 1:
    if ser.in_waiting > 0:
        line = ser.readline().decode("utf-8").rstrip()
        print(line)
