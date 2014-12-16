''' Espesificaciones
Dispositivo:
Dos Displays Anodo Comun
Puerto Paralelo
Conexiones:
Salida 1: Pin A ( Display )
Salida 2: Pin B ( Display )
Salida 3: Pin C ( Display )
Salida 4: Pin D ( Display )
Salida 5: Pin E ( Display )
Salida 6: Pin F ( Display )
Salida 7: Pin G ( Display )
Salida 8: Pin VCC ( Display )
Objectivo:
Recorrer del 1 al 100 Multiplexado
'''
import parallel
import time
p = parallel.Parallel()
numeroDisplay = (192,249,164,176,153,146,130,248,128,152)
display1Num = 0
display2Num = 0
timeCount = 0
while(1 == 1):
	display2Num = display2Num + 1
	if(display2Num == 10):
		#print "Igual a 10"
		display2Num = 0
		display1Num = 1 + display1Num
	if(display1Num == 10):
		display1Num = 0
	print "%d%d" % (display1Num,display2Num)
	'''if(display1Num > 9 and display2Num < 9):
		print "%d:0%d" % (display1Num,display2Num)
	elif (display1Num < 9 and display2Num > 9):
		print "0%d:%d" % (display1Num,display2Num)
	elif (display1Num < 9 and display2Num < 9):
		print "0%d:0%d" % (display1Num,display2Num)
	elif (display1Num > 9 and display2Num > 9):
		print "%d:%d" % (display1Num,display2Num)'''
	
	while( 1 == 1 ):
		timeCount = timeCount + 1
		if ( display2Num < 10 ) :		
			#print display2Num
			resta = numeroDisplay[display2Num] - 128
			p.setDataStrobe(1)
			p.setData(resta)
		time.sleep(.01)
		if( display1Num < 10):
			p.setDataStrobe(0)
			p.setData(numeroDisplay[display1Num])
		time.sleep(.01)
		if(timeCount == 50):
			timeCount = 0
			break;
	
	
