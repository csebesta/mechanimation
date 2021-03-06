import serial
import time

# Serial port configuration
ser = serial.Serial()
ser.port = 'COM3'
ser.baudrate = 4800
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.open()

# Check configuration
print ser.portstr # Check port in use
print "baudrate =", ser.baudrate
print "bytesize =", ser.bytesize
print "parity =", ser.parity
print "stopbits =", ser.stopbits

data = 225
# Send data continuously
while ser.isOpen():
    ser.write(chr(data))
    time.sleep(.1)
    #ser.close()
