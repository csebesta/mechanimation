import serial

# Serial port configuration
ser = serial.Serial()
ser.port = 'COM3'
ser.baudrate = 4800
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.open()
print(ser.portstr) # Check port in use
print("baudrate =", ser.baudrate)
print("bytesize =", ser.bytesize)
print("parity =", ser.parity)
print("stopbits =", ser.stopbits)

# Send data continuously
while ser.isOpen():
    ser.write(bytes('150', 'ascii'))
    #ser.close()
