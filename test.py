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

Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/serial/serialposix.py", line 322, in open
    self.fd = os.open(self.portstr, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
PermissionError: [Errno 13] Permission denied: '/dev/serial0'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/pi/Desktop/JinhangBank/Website/App.py", line 10, in <module>
    app = create_app()
  File "/home/pi/Desktop/JinhangBank/Website/views/__init__.py", line 23, in create_app
    from .bePatient import bePatient_bp
  File "/home/pi/Desktop/JinhangBank/Website/views/bePatient.py", line 8, in <module>
    ser = serial.Serial("/dev/serial0", 9600)  # check your COM port and baud rate
  File "/usr/lib/python3/dist-packages/serial/serialutil.py", line 244, in __init__
    self.open()
  File "/usr/lib/python3/dist-packages/serial/serialposix.py", line 325, in open
    raise SerialException(msg.errno, "could not open port {}: {}".format(self._port, msg))
serial.serialutil.SerialException: [Errno 13] could not open port /dev/serial0: [Errno 13] Permission denied: '/dev/serial0'