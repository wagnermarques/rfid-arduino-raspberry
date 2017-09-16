import RPi.GPIO as GPIO

# Configura modo de definicao de pinos como BOARD, ou seja, contagem de pinos da placa
GPIO.setmode(GPIO.BOARD)

#Desativa warnings
GPIO.setwarnings(False)

pinVermelho = 7
pinVerde = 11

#Configura pino 18 da placa (GPIO24) como saida
GPIO.setup(pinVermelho,GPIO.OUT)
GPIO.setup(pinVerde,GPIO.OUT)

statusLedVermelho = False
statusLedVerde = False

def ascende_led_verde():
    GPIO.output(pinVerde, GPIO.HIGH)    
    statusLedVerde= True
    print("led verde encontra-se asceso")
    
def apaga_led_verde():
    GPIO.output(pinVerde, GPIO.LOW)    
    statusLedVerde = False
    print("led verde encontra-se apagado")

def ascende_led_vermelho():
    GPIO.output(pinVermelho, GPIO.HIGH)
    statusLedVermelho = True
    print("led vermelho encontra-se asceso")

def apaga_led_vermelho():
    GPIO.output(pinVermelho, GPIO.LOW)
    statusLedVervelhor = False
    print("led vermelho encontra-se apagado")

#ascende_led_vermelho()
#apaga_led_vermelho()
#ascende_led_verde()
#apaga_led_verde()
