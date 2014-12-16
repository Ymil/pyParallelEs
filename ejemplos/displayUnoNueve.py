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
Recorrer del 1 al 9
'''
import parallel
import time
p = parallel.Parallel()
numeroDisplay = (249,164,176,153,146,130,248,128,152)
while(1 == 1):
	p.setData(numeroDisplay[numeroBucle])
	numeroBucle = numeroBucle + 1
	if ( numeroBucle == 9):
		numeroBucle = 0
	time.sleep(0.3)
	
