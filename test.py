import serial

bills = [10, 20, 30]
# Start serial communication
ser = serial.Serial("/dev/ACM0", 9600)  # check your COM port and baud rate

ser.write("1")
