import serial

run = True
while run:
    ser = serial.Serial('COM3', 4800)  # open first serial port
    #print(ser.portstr)      # check which port was really used
    ser.write(bytes("150", 'ascii'))      # write a string
    ser.close()             # close port
