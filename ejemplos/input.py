import parallel, time
p = parallel.Parallel()
count = 0
while( 1 == 1):
	p.setData(0x0)
	time.sleep(0.2)
	p.setData(0xFF)
	time.sleep(0.2)
	'''if(p.getInSelected() == 0):
		p.setData(0xFF)
		print("Led encendido")
	else:
		p.setData(0x0)'''