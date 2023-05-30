import serial

bills = [10, 20, 30]
# Start serial communication
ser = serial.Serial("/dev/serial0", 9600)  # check your COM port and baud rate

ser.write(str(bills).encode())
