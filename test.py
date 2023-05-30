import serial
import time


def send_to_arduino(arduino, message):
    arduino.write(message.encode())


def get_ack_from_arduino(arduino):
    ack = arduino.readline().decode().strip()  # Strip to remove trailing newline
    print(f"Received from Arduino: {ack}")


arduino_uno = serial.Serial("/dev/ttyACM0", 9600)  # Update with your Mega's device name
arduino_mega = serial.Serial("/dev/ttyACM1", 9600)  # Update with your Uno's device name

time.sleep(2)  # Waiting for the Arduino to initialize

send_to_arduino(arduino_mega, "Hello, Mega!")
get_ack_from_arduino(arduino_mega)

send_to_arduino(arduino_uno, "Hello, Uno!")
get_ack_from_arduino(arduino_uno)

arduino_mega.close()
arduino_uno.close()
