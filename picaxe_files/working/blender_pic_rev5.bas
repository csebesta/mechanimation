; Chad Sebesta
; Blender_pic

; Initialization
init:
dirsc = %00000111
pinsc = %00000000
b0 = 150 ; Servo pulse width
b1 = 0 ; Centering routine
for b1 = 0 to 30
	pulsout c.1, b0
	pulsout c.2, b0
	pause 20
next b1
pause 1000

; Main block
main:
serrxd b0
if b0 < 75  or b0 > 225 then
	high c.0
	pause 250
	low c.0
	goto main
endif
pulsout c.1, b0
pulsout c.2, b0
pause 20
goto main