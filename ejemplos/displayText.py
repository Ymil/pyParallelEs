''' Espesificaciones
Dispositivo:
Display Anodo Comun
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
Escribir el Texto "Hola" en un Display de 7 Segmentos
'''

import parallel
import time
import binarioDisplay #Libreria binenarioDisplay.py

p = parallel.Parallel()
b = binarioDisplay
letras = {"h": b.displayNum(0,0,0,1,0,0,1),
	"o": b.displayNum(1,0,0,0,0,0,0),
	"l": b.displayNum(1,0,0,0,1,1,1),
	"a": b.displayNum(0,0,0,1,0,0,0)
}

palabra = "hola"
while( 1 == 1 ):
	for letra in palabra:
		p.setData(letras[letra])
		time.sleep(0.5)
	time.sleep(0.5)