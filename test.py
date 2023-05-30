import serial
import time

ser = serial.Serial(
    port="/dev/serial0",  # Change this as per your port name
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1,
)

# give the serial connection a second to settle
time.sleep(1)

try:
    ser.write(b"1")
    print("Sent '1' to Arduino")
except Exception as e:
    print("Error occurred: ", e)
finally:
    ser.close()
