#display2.py
import parallel
import time
p = parallel.Parallel()
numeroDisplay = (249,164,176,153,146,130,248,128,152)
numeroBucle = 0
while(1 == 1):
	if(p.getInSelected() == 0):
		p.setData(numeroDisplay[numeroBucle])
		numeroBucle = numeroBucle + 1
		if ( numeroBucle == 9):
			numeroBucle = 0
		time.sleep(0.3)
	
