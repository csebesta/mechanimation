import ftplib
import urllib2
import serial, time
from datetime import datetime
format = "%Y-%m-%d %H:%M"
##
##Change the COM port number here!
ser = serial.Serial('COM3', 9600, timeout=1)

while True:
##Send data request to picaxe
    ser.write("xxxxxx")      #write a string
    tm2 = datetime.now().strftime(format+":%S")
    tmin = int(datetime.now().strftime("%M"))
    tmod = tmin%5
    print ("Data Requested: " + tm2)
    time.sleep(2)  #give the serial port sometime to receive the data
##Put received data into qs
    qs = ser.readline()
    if len(qs) > 0:
        print("Data Received: " + qs)
        t3 = int(qs)
        if (t3 > 32768):
            t3 = t3 - 65536
        t4 = str(round(float(t3 * .0625)*1.8+32,2))
        print ("DS18B20 Temp " + t4)
        print (" ")
    time.sleep(5)    
