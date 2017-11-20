import time
import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

pinTravaEntrada = 12;
pinTravaSaida = 13;

GPIO.setup(pinTravaEntrada,GPIO.OUT)
GPIO.setup(pinTravaSaida,GPIO.OUT)

#def destrava_catraca():



#def trava_catraca():
#GPIO.output(pinTravaEntrada, GPIO.HIGH)    
#GPIO.output(pinTravaSaida, GPIO.LOW)    
GPIO.output(pinTravaEntrada, GPIO.HIGH)    
#GPIO.output(pinTravaSaida, GPIO.HIGH)    
