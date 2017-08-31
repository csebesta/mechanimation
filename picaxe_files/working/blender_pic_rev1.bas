; Chad Sebesta
; Blender_pic

; Initialization
init:
dirsc = %00000111
pinsc = %00000000
b0 = 0 ; Hundreds
b1 = 0 ; Tens
b2 = 0 ; Ones
b3 = 150 ; Servo pulse width
servo c.1, b3

; Main block
main:
'sertxd ("Enter a pulse width of the form XXX, where X is a digit ...", 10, 13)
serrxd  b0, b1, b2
let b0 = b0 - 48 * 100
let b1 = b1 - 48 * 10
let b2 = b2 - 48
let b3 = b0 + b1 + b2
if b3 < 75  or b3 > 225 then
	sertxd ("Out of range!", 10, 13, 10, 13)
	pinsc = %00000000
	goto main
endif
servopos c.1, b3
pause 2000
'sertxd ("Servo pulse width is now: ", #b3, 10,13, 10, 13)
goto main