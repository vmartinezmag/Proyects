import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
p= GPIO.PWM(7,50)
p.start(3.5)
while True:
	print time.strftime("%I:%M")
	print ("introduce la hora que se va a despachar el alimento")
	hora = '0'
	hora += str(input("Hora:\n"))
	hora += str(input("Minutos:\n"))
	print(hora)
	bandera = False
	try:
		while True:
			horas = time.strftime("%I%M")
			print time.strftime("%I:%M:%S")
			time.sleep(0.5)
			if(horas == hora and bandera == False ):
				p.ChangeDutyCycle(6.5)
				time.sleep(1)
				bandera = True
			p.ChangeDutyCycle(3.5)
			time.sleep(0.5)
			if(bandera == True):
				break
#    	time.sleep(1)12.5
#        GPIO.output(7,True)
#        time.sleep(0.005)
#        GPIO.output(7,False)
#        time.sleep(0.001)

	except KeyboardInterrupt:
		p.stop()
		GPIO.cleanup()
