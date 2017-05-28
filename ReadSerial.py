import serial


# G L O B A L   V A R S 
duino_dev = '/dev/ttyACM0'
card_id = None



# S E T U P    S E R I A L
try:
    ser = serial.Serial(
        port=duino_dev,
        baudrate=9600,
        bytesize=serial.SEVENBITS,
        parity=serial.PARITY_EVEN,
        stopbits=serial.STOPBITS_ONE,
        timeout=0.1
    )

    # try to open port, if possible print message and proceed with 'while True:'
    # tenta abrir a porta serial do arduino
    # se der printa a msg e continua
    # caso contrario cai no except
    ser.isOpen() 

except IOError:
    # Se o metodo isOpen() falhar, tentamos fechar e abrir de novo
    ser.close()
    ser.open()





# Pode ser que a porta ja esteja aberta
# Se for o caso, a gente toma o erro
# raise SerialException("Port is already open.")
# com esse try, a exception pode ser gerenciada
# try:
#    ser.open()
# except:
#    pass



# L O O P  D E  I N T E R A C A O   C O M   O   A R D U I N O
while True:
    bytes_lidos = ser.readline()

    if (bytes_lidos == b''):
        pass
    else:
        pass
