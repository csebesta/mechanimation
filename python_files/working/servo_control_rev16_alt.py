import serial
import time
import bpy
import math
from math import degrees

# Serial port configuration
ser = serial.Serial()
ser.port = 'COM3'
ser.baudrate = 4800
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
#ser.timeout = 1
ser.open()

# Check configuration
print(ser.portstr) # Check port in use
print("baudrate =", ser.baudrate)
print("bytesize =", ser.bytesize)
print("parity =", ser.parity)
print("stopbits =", ser.stopbits)

# Range checking
def remap( x, oMin, oMax, nMin, nMax ):

    # Range check
    if oMin == oMax:
        print("Warning: Zero input range")
        return None

    if nMin == nMax:
        print("Warning: Zero output range")
        return None

    # Check reversed input range
    reverseInput = False
    oldMin = min( oMin, oMax )
    oldMax = max( oMin, oMax )
    if not oldMin == oMin:
        reverseInput = True

    # Check reversed output range
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

# Servo control
def my_handler(scene):

    # Servo pan
    servo_pan = bpy.data.objects['Cube'].rotation_euler.x
    servo_pan = degrees(servo_pan)
    servo_pan = remap(servo_pan, -90, 90, 75, 225)
    servo_pan = int(servo_pan)

    # Servo tilt
    servo_tilt = bpy.data.objects['Cube'].rotation_euler.x
    servo_tilt = degrees(servo_tilt)
    servo_tilt = remap(servo_tilt, -90, 90, 75, 225)
    servo_tilt = int(servo_tilt)    

    # Write rotation to serial port
    ser.write(bytes(str(chr(servo_pan)), encoding='latin-1'))
    ser.write(bytes(str(chr(servo_tilt)), encoding='latin-1'))

    # Pause to allow device to respond
    time.sleep(.02)

    # Display current servo pulse
    print("Servo pan =", servo_pan)
    print("Servo tilt =", servo_tilt)

# Execute function on every frame
bpy.app.handlers.frame_change_post.append(my_handler)
