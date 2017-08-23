import bpy
import math
from math import degrees
import serial

# Create a persistent connection to COM port 6
ser = serial.Serial('COM3',4800,timeout=1)

def my_handler(scene):
    
    # Get the Euler x rotation in degrees.  The rotation for "Cube" will be applied to servo on pin 9
    servoAngle9 = degrees(bpy.data.objects['Cube'].rotation_euler.x)
    
    # Get the Euler x rotation in degrees.  The rotation for "Cube1" will be applied to the servo on pin 10
    servoAngle10 = degrees(bpy.data.objects['Cube1'].rotation_euler.x)
    
    # Convert these values into a byte array.
    data = bytes( [9, int(servoAngle9), 10, int(servoAngle10)] )
    
    # Write the commands to the serial port.
    ser.write(data)
    
# Register the handler to be called once the frame has changed.
bpy.app.handlers.frame_change_post.append(my_handler)
