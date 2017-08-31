; Initialization
init:
dirsc = %00000111
pinsc = %00000000
b0 = 75
b1 = 0

; Main block
main:
sertxd (b0)
if b0 = 75 then
	toggle c.2
	pause 2000
endif
goto main