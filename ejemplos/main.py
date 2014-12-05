'''Codigo de ejemplo Puerto Paralelo con Python'''
'''Por Lautaro Linquimán Site: detodounpocopcs.com'''
import parallel
import time
p = parallel.Parallel() #Instancia al puerto paralelo
p.setData(0x0)#Apagamos los leds
timeBucle = 0.5 #Tiempo de cada led Prendido
while( 1 == 1 ): #Buble infinito de encendido
	p.setData(0x40) 
	time.sleep(timeBucle)
	p.setData(0x8)
	time.sleep(timeBucle)
	p.setData(0x1)
	time.sleep(timeBucle)
	p.setData(0x8)
	time.sleep(timeBucle)