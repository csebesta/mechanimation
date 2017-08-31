import serial
ser = serial.Serial()
ser.baudrate = 4800
ser.timeout = 100
ser.port='COM3' #change to correct port number
ser.open()
line = ""
while line == "":
    line = ser.readline() #read a '\n' terminated line
    print(line.strip())
    ser.close()
