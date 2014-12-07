import parallel
import time
def number(n,d = 0): 
	'''Devuelve el valor decimal de los pines que se quieran preden empezando del A
	Ejemplo: number(1) = 251'''
	#print d
	total = 0
	for x in range (d, n ):
		total = total+ 2**x		
	dec = 255-total
	return dec
def displayNum ( g,f,e,d,c,b,a ):
	dex = 255
	resultado = 0
	if(a == 0):
		resultado = resultado + 2**0
	if (b == 0):		
		resultado = resultado + 2**1
	if (c == 0):
		resultado = resultado + 2**2
	if (d == 0):
		resultado = resultado + 2**3
	if (e == 0):
		resultado = resultado + 2**4
	if (f == 0):
		resultado = resultado + 2**5
	if (g == 0):
		resultado = resultado + 2**6
	#print resultado
	return dex - resultado
		
p = parallel.Parallel()
uno = displayNum(1,1,1,1,0,0,1)
dos = displayNum(0,1,0,0,1,0,0)
tres = displayNum(0,1,1,0,0,0,0)
cuatro = displayNum(0,0,1,1,0,0,1)
cinco = displayNum(0,0,1,0,0,1,0)
seis = displayNum(0,0,0,0,0,1,0)
siete = displayNum(1,1,1,1,0,0,0)
ocho = displayNum(0,0,0,0,0,0,0)
nueve = displayNum(0,0,1,1,0,0,0)
numeros = (uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve)
'''while(1 == 1):
	x = raw_input("N")
	d = raw_input("D")
	if (len(d) == 0):
		d = 0'''
for x in numeros:
	print x
	p.setData(x)
	time.sleep(1)
