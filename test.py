import serial
import time


def send_to_arduino(arduino, message):
    arduino.write(message.encode())


arduino_mega = serial.Serial(
    "/dev/ttyACM0", 9600
)  # Update with your Mega's device name
arduino_uno = serial.Serial("/dev/ttyACM1", 9600)  # Update with your Uno's device name

time.sleep(2)  # Waiting for the Arduino to initialize

send_to_arduino(arduino_mega, "Hello, Mega!")
send_to_arduino(arduino_uno, "Hello, Uno!")

arduino_mega.close()
arduino_uno.close()
