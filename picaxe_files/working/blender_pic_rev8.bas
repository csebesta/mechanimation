; Chad Sebesta
; Blender_pic

; Initialization
init:
dirsc = %00010111
pinsc = %00010000


b0 = 150 ; Initial pulse width
b1 = 0 ; Servo pan
b2 = 0 ; Servo tilt
b27 = 0 ; Centering routine

; Centering routine
for b27 = 0 to 30
	pulsout c.1, b0
	pulsout c.2, b0
	pause 20
next b27
pause 1000

; Main block
main:
serrxd b1, b2
if b1 < 75 or b1 > 225 then
	high c.0
	pause 250
	low c.0
	goto main
endif
if b2 < 125 or b2 > 225 then
	high c.0
	pause 250
	low c.0
	goto main
endif
pulsout c.1, b1
pulsout c.2, b2
pause 20
goto main