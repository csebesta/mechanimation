# Get serial module
import serial

# Define com port
usbport = 'COM3'

# Configure connection
ser = serial.Serial(usbport, 4800)

run = True
while run:
    ser.write(150)

