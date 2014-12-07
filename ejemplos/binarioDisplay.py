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