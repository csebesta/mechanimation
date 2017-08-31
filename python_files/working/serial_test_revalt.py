import serial

# Serial port configuration
ser = serial.Serial()
ser.port = 'COM3'
ser.baudrate = 4800
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.open()

# Check configuration
print(ser.portstr) # Check port in use
print("baudrate =", ser.baudrate)
print("bytesize =", ser.bytesize)
print("parity =", ser.parity)
print("stopbits =", ser.stopbits)

data = 75
# Send data continuously
while ser.isOpen():
#ser.write(str.encode(chr(75)))
#ser.write((75).int_tobytes(2,'big',signed=True))
    ser.write(data)
    #ser.close()
