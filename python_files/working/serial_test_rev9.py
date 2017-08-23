import serial
import time

"""#fimport bpy
import math
from math import degrees
import serial"""

def remap( x, oMin, oMax, nMin, nMax ):

    #range check
    if oMin == oMax:
        print "Warning: Zero input range"
        return None

    if nMin == nMax:
        print "Warning: Zero output range"
        return None

    #check reversed input range
    reverseInput = False
    oldMin = min( oMin, oMax )
    oldMax = max( oMin, oMax )
    if not oldMin == oMin:
        reverseInput = True

    #check reversed output range
    reverseOutput = False   
    newMin = min( nMin, nMax )
    newMax = max( nMin, nMax )
    if not newMin == nMin :
        reverseOutput = True

    portion = (x-oldMin)*(newMax-newMin)/(oldMax-oldMin)
    if reverseInput:
        portion = (oldMax-x)*(newMax-newMin)/(oldMax-oldMin)

    result = portion + newMin
    if reverseOutput:
        result = newMax - portion

    return result

"""
def my_handler(scene):
    data = ''
    eulx = bpy.data.objects['Cube'].rotation_euler
    x = degrees(eulx.x)
    data = bytes([int(x)])
    ser.write(data)
bpy.app.handlers.frame_change_post.append(my_handler)
"""

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

# Initial value of x
x = 0

# Send data continuously
while ser.isOpen():
    #x = int(raw_input("Enter a value: "))
    data = remap(x, -90, 90, 75, 225)
    ser.write(chr(data))
    time.sleep(.1)
    #ser.close()
