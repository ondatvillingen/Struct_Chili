import serial
serialport = serial.Serial("/dev/tty.usbmodem411", 9600, timeout= 2)
response = serialport.readlines(None)
print response
