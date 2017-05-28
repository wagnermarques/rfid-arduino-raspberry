import time
import datetime
import serial
import sqlite3Commands as dbCmd
import arduinoCommands as duinoCmd

import model


# S E T U P   D A T A B A S E

# criando o banco de dados caso ele nao exista
# este metodo usa create if exists
# portanto se a tabela ja existir nao cria de novo
dbCmd.create_table()


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
    str_lida = bytes_lidos.decode()    
    strCard_uid = str_lida.strip()

    if (bytes_lidos == b''):
        pass

    # https://stackoverflow.com/questions/9573244/most-elegant-way-to-check-if-the-string-is-empty-in-python
    elif (strCard_uid):
        # um registro representa a passagem do cartao
        # independente se essa passagem de cartao identifica realmente
        # uma pessoa ou nao, esse registro sera salvo no banco
        objRegistro = model.Registro(datetime.datetime.today(), strCard_uid , 0)

        # o resultado indica se a pessoa foi identificada ou nao
        # se o resultVerificacao for None, significa que nao se identificou uma pessoa
        resultVerificacao = dbCmd.verifica_pessoa_cadastrada_by_id_card(strCard_uid)
        
        if (resultVerificacao is not None):
            objPessoaVerificada = resultVerificacao
            # esse um significa que a pessoa esta corretamente identificada
            objRegistro.autorizado = 1
            print(resultVerificacao)
        else:
            print("Nao Identificado")
            # resultVerificacao vale None
            # entao nao ganha o 1 de verdade ref a verificacao
            
        # Apos verificar se a verificacao no banco...
        # A passagem do cartao he registrada, tenho sido a pessoa autorizada
        # ou seja, identificada corretamente
        # ou nao.
        dbCmd.insert_into_registro(objRegistro)
