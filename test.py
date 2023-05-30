import serial
import time


def send_to_arduino(arduino, message):
    arduino.write(message.encode())


def get_ack_from_arduino(arduino):
    ack = arduino.readline().decode().strip()  # Strip to remove trailing newline
    print(f"Received from Arduino: {ack}")


def get_button_press_from_mega(arduino):
    while True:
        if arduino.in_waiting > 0:
            button_press = (
                arduino.readline().decode().strip()
            )  # Strip to remove trailing newline
            print(f"Button {button_press} was pressed on the Arduino Mega")


arduino_mega = serial.Serial("/dev/ttyACM0", 9600)  # Update with your Uno's device name
arduino_uno = serial.Serial("/dev/ttyACM1", 9600)  # Update with your Mega's device name

time.sleep(2)  # Waiting for the Arduino to initialize

get_button_press_from_mega(arduino_mega)

arduino_mega.close()
arduino_uno.close()
