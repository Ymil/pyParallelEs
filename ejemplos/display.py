import parallel
import time
p = parallel.Parallel()
a = 0xFE
b = 0xFD
c = 0xFB
d = 0xF7
e = 0xEF
f = 0xDF
g = 0xBF
onAll = 255
leds = [0xFE,0xFD,0xFB,0xF7,0xEF,0xDF,0xBF]
def readLeds ():
	for ledOn in leds:
		p.setData(ledOn)
		print ledOn
		time.sleep(0.01);
while ( 1 == 1): 
	#time.sleep(0.5)
	if (p.getInSelected() == 0):
		readLeds()
		

