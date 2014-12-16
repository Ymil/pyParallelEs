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
import binarioDisplay 
import sys
p = parallel.Parallel()

print "Hola"

palabra = "hola"
	
b = binarioDisplay
letras = {"h": b.displayNum(0,0,0,1,0,0,1),
	"o": b.displayNum(1,0,0,0,0,0,0),
	"l": b.displayNum(1,0,0,0,1,1,1),
	"a": b.displayNum(0,0,0,1,0,0,0),
	" ": b.displayNum(1,1,1,1,1,1,1),
	"e": b.displayNum(0,0,0,0,0,1,1),
}
registro = 0
display1Letra = 0
display2Letra = 0
timeCount = 0
timeCountRepeat = 25
timeSleep = .01
reinicioLetras = 0
while(1 == 1):		
	if(registro == 0):
		display2Letra = palabra[registro]
		display1Letra = 0
	elif ( registro == len(palabra)):
		display1Letra = palabra[len(palabra)-1]
		display2Letra = 0
		reinicioLetras = 1
		print "Llegamos!"		
	else:		
		display2Letra = palabra[registro]
		display1Letra = palabra[registro-1]
	
	#print "Registro %d" % registro
	while(1 == 1):
		timeCount = timeCount + 1
		if ( not display2Letra == 0 ):
			p.setDataStrobe(1)
			resultado = letras[display2Letra] - 128
			p.setData(resultado)
		time.sleep(timeSleep)
		p.setDataStrobe(0)
		
		if ( not display1Letra == 0):
			p.setDataStrobe(0)
			p.setData(letras[display1Letra])			
		time.sleep(timeSleep)
		p.setData(0)
		if(timeCount == timeCountRepeat):
			timeCount = 0
			if (not display2Letra == 0):
				print "%d" % (letras[display2Letra] - 128)
			break;
			
		#print "%s%s" % ( display1Letra, display2Letra )
	if(reinicioLetras == 1):
		registro = 0
		reinicioLetras = 0
	else:
		registro = registro + 1	
	'''display2Num = display2Num + 1
	if(display2Num == 10):
		#print "Igual a 10"
		display2Num = 0
		display1Num = 1 + display1Num
	if(display1Num == 10):
		display1Num = 0
	print "%d%d" % (display1Num,display2Num)'''
	'''if(display1Num > 9 and display2Num < 9):
		print "%d:0%d" % (display1Num,display2Num)
	elif (display1Num < 9 and display2Num > 9):
		print "0%d:%d" % (display1Num,display2Num)
	elif (display1Num < 9 and display2Num < 9):
		print "0%d:0%d" % (display1Num,display2Num)
	elif (display1Num > 9 and display2Num > 9):
		print "%d:%d" % (display1Num,display2Num)'''
	'''
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
			break;'''
