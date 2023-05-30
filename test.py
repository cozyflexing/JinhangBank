# views/arduinoInput.py
import serial

arduino_mega = serial.Serial("/dev/ttyACM0", 9600)  # Update with your Uno's device name


while 1:
    if arduino_mega.in_waiting > 0:
        line = arduino_mega.readline().decode("utf-8").rstrip()
        print(line)
