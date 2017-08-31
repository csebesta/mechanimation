; Initialization
init:
dirsc = %00000111
pinsc = %00000000
b0 = 0

; Main block
main:
serrxd b0
if b0 = 49 then
	toggle c.2
	pause 2000
endif
goto main