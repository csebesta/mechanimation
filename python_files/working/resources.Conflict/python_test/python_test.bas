' PICAXE-20X2              

#picaxe 20x2
#Terminal 9600
#No_Table
#No_Data


Symbol Lo = B20
Symbol Hi = B21
Symbol PEC = B2
Symbol Status = B3
Symbol Val = W3
Symbol Chk = W4
Symbol SlaveAdr_2 = B10
Symbol RamLocation = B11
Symbol X = B12
Symbol N = B13
Symbol CRC8 = B14
Symbol Heat = W8
Symbol LED = B.0
Symbol DS18B20 = C.4

Top:

	hsersetup b9600_8, %00 ' set the serial output to 9600 baud
	
Again:
'read ambient temp from DS18B20
	ReadTemp12 DS18B20, w0
	SerTxd ("DS18B20 Temp Code ")
	SerTxd (#w0)
	SerTxd( CR, LF )
'wait for request from PC and go to whoops if it doesn't arrive before timeout
	SerTxd ("waiting for data request")
	SerTxd( CR, LF )
	hserin [10000,whoops],0,4,("x")
	SerTxd ("PC has requested data")
 	SerTxD (CR, LF)
'send ambient temp
	SerTxD ("Sending data to PC")
	hserout 0,(#w0)
	SerTxD (CR, LF)
'send new line code
	hserout 0,(CR, LF)
'wait a while and do it again
	Pause 20
	GoTo Again
whoops:
	SerTxd ("timeout")
	SerTxd (CR, LF)   
	Pause 20
	GoTo Again
      