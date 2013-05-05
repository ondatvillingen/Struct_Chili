import serial

# change serial.port name to: ttyAMA0 for raspberry pi

while True:
	try: 
		serialport = serial.Serial("/dev/tty.usbmodem411", 9600, timeout= 0.5)
		break
	except: 
		print "Serial Error"
		exit(0)
response = serialport.readlines(None)
print response

