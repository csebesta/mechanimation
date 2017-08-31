import serial
import time
import bpy
import math
from math import degrees

# Range checking
def remap( x, oMin, oMax, nMin, nMax ):

    #range check
    if oMin == oMax:
        print("Warning: Zero input range")
        return None

    if nMin == nMax:
        print("Warning: Zero output range")
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


def my_handler(scene):
    
    # Get the Euler x rotation in degrees.  The rotation for "Cube" will be applied to servo on pin 9
    servoAngle = degrees(bpy.data.objects['Cube'].rotation_euler.x)
 
    # Convert these values into a byte array.
    sa = int(servoAngle)
    
    # Register the handler to be called once the frame has changed.
    bpy.app.handlers.frame_change_post.append(my_handler)


"""# Blender script
def my_handler(scene):
    bdata = ''
    eulx = bpy.data.objects['Cube'].rotation_euler
    bx = degrees(eulx.x)
    data = bytes([int(bx)])
    ser.write(bdata)
bpy.app.handlers.frame_change_post.append(my_handler)"""

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

# Initial value of x
x = remap(0, -90, 90, 75, 225)

# Send data continuously
while ser.isOpen():
    #x = int(raw_input("Enter a value: "))
    #data = remap(x, -90, 90, 75, 225)
    ser.write((bytes(str(x), 'ascii')))
    time.sleep(.1)
    my_handler(scene)
    #ser.close()
