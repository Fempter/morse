import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)

GPIO.output(18,True)
GPIO.output(18,False)

morse = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..'}

wyraz = raw_input('Podaj litere: ')
wynik = ""

for i in range(len(wyraz)):
	kod = morse[wyraz[i]]
	wynik += kod + '|'

print wynik

for i in wynik:
	print i
	if i == '-':
		GPIO.output(18,True)
		time.sleep(0.6)
		GPIO.output(18,False)
		time.sleep(0.4)
	elif i =='.':
		GPIO.output(18,True)
		time.sleep(0.2)
		GPIO.output(18,False)
		time.sleep(0.4)
	else:
		time.sleep(0.5)
	
GPIO.cleanup()
