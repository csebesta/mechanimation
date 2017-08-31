; Chad Sebesta
; Blender_pic

; Initialization
init:
dirsc = %00000111
pinsc = %00000000
b0 = 150 ; Servo pulse width]
servo c.1, b0
pause 1000

; Main block
main:
serrxd b0
if b0 < 75  or b0 > 225 then
	high c.2
	pause 250
	low c.2
	goto main
endif
servopos c.1, b0
pause 20
goto main