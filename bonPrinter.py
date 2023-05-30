import serial
import time

# Replace '/dev/serial0' with the port that your Adafruit printer is connected to
ser = serial.Serial("/dev/serial0", 19200, timeout=1)

# Wake the printer
ser.write(bytearray([0x1B, 0x40]))

time.sleep(0.5)

# Write "Hello, world!" to the printer
ser.write(b"Hello, world!\n")

# Feed three lines to give some space
ser.write(bytearray([0x1B, 0x64, 0x03]))

ser.close()
