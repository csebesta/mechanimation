; Chad Sebesta
; Blender_pic

; Initialization
init:
dirs = %00000111
pins = %00000000
b0 = 150 ; Servo pulse width
b1 = 0 ; Centering routine
for b1 = 0 to 30
	pulsout 1, b0
	pulsout 2, b0
	pause 20
next b1
pause 1000

; Main block
main:
serin 4,4800, b0
if b0 < 75  or b0 > 225 then
	high 0
	pause 250
	low 0
	goto main
endif
pulsout 1, b0
pulsout 2, b0
pause 20
goto main