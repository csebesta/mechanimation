import serial

# Serial port configuration
ser = serial.Serial()
ser.port = 'COM3'
ser.baudrate = 4800
ser.open()

# Send data continuously
while ser.isOpen():
    #print(ser.portstr)      # check which port was really used
    ser.write(bytes("150", 'ascii'))      # write a string
    #ser.close()             # close port
