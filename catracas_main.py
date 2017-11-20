import time
import datetime
import serial
import sqlite3Commands as dbCmd
import arduinoCommands as duinoCmd
import trava_catraca as catrCmd
import ledCommands as ledCmd
#import traceback
import model


# S E T U P   D A T A B A S E

# criando o banco de dados caso ele nao exista
# este metodo usa create if exists
# portanto se a tabela ja existir nao cria de novo
dbCmd.create_table()


# G L O B A L   V A R S
duino_dev = '/dev/ttyACM0'
#duino_dev = '/dev/ttyUSB0'
card_id = None
tempo_de_releitura_do_serial_do_arduino = 1
tempo_de_espera_da_catraca_liberada_pra_pessoa_passar = 2


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

    # tenta abrir a porta serial do arduino
    # caso contrario cai no except
    ser.isOpen()
except IOError:
    # Se o metodo isOpen() falhar, tentamos fechar e abrir de novo
    traceback.print_exc();
    ser.close()
    ser.open()


    #FUNCS QUE TRATAM DE USUARIO AUTENTICADO E NAO ATENTICADO
def handle_leitura_de_pessoa_autenticada(id_card,objPessoaAutenticada):
    print("Autenticada :"+id_card+"PessoaAutenticada:"+objPessoaAutenticada.nome+"\n")
    

def handle_leitura_de_pessoa_nao_autenticada(id_card):
    print("Nao Autenticada :" + id_card+"\n")
    

    # L O O P  D E  I N T E R A C A O   C O M   O   A R D U I N O
ledCmd.ascende_led_vermelho()    
while True:
    bytes_lidos = ser.readline()
    str_lida = bytes_lidos.decode()    
    leitura = str_lida.strip()
    
    if (bytes_lidos == b''):
        pass

    # https://stackoverflow.com/questions/9573244/most-elegant-way-to-check-if-the-string-is-empty-in-python
    elif (leitura):

        leitura_partes = leitura.split("|")
        leitura_parte1 = leitura_partes[0].strip()
        leitura_parte2 = leitura_partes[1].strip()
         
        #Dentro desse if a gente so trata leituras de cartao e nenhuma outra msg que vem do arduino
        if(leitura_parte1 == "msg_card_uid"):
            #Se a primeira parte da leitura e msg_card_uid, a segunda e obviamente o card_uid
            id_card = leitura_parte2

            
            # um registro representa a passagem do cartao
            # independente se essa passagem de cartao identifica realmente
            # uma pessoa ou nao, esse registro sera salvo no banco
            objRegistro = model.Registro(datetime.datetime.today(), id_card, 0)

            # o resultado indica se a pessoa foi identificada ou nao
            # se o resultVerificacao for None, significa que nao se identificou uma pessoa
            objPessoaAutenticada = dbCmd.verifica_pessoa_cadastrada_by_id_card(id_card)
            if (objPessoaAutenticada is not None):
                # esse 1 significa que a pessoa esta corretamente identificada
                objRegistro.autorizado = 1
                ledCmd.apaga_led_vermelho()
                ledCmd.ascende_led_verde()                
                # Na linha abaixo a gente diz pro registro da passagem do cartao qual foi o id da pessoa que foi identificada
                objRegistro.id_pessoa_identificada = objPessoaAutenticada.matricula
                handle_leitura_de_pessoa_autenticada(id_card,objPessoaAutenticada)
                time.sleep(tempo_de_espera_da_catraca_liberada_pra_pessoa_passar)
                #ledCmd.apaga_led_verde()
                #pensando bem vou apagar la em baixo,
                #pra dar um tempo pra pessoa passar na catraca
                #ou simplesmente prover alguns segundos
                #pra pessoa perceber o led verde
            else:
                #handling pessoa nao autorizada
                #print("Nao Identificado:" + str(datetime.datetime.now()))
                #ledCmd.ascende_led_vermelho()
                #nao autorizada o led vermelho ja estava asceso mesmo...
                #Considerando que mesmo que a leitura de pessoa nao autorizada tambem e registrada no banco
                #Tem que ficar esperto porque nao vamos registrar cada leitura feita por este loope while
                #porque seriam muitas leituras repetidas. Entao a gente que que ignorar algumas leituras
                #Considerando que da umas 20 leituras por segundo, podemos igrnorar umas 15 leituras, por exemplo
                #Desprezamos 15 e gravamos 5...
                #Essa logica vai ficar a cargo dessa funcaozinha abaixo
                handle_leitura_de_pessoa_nao_autenticada(id_card) #leitura_parte2 nesta parte do co
                time.sleep(tempo_de_releitura_do_serial_do_arduino)
                #ledCmd.apaga_led_vermelho() vou manter o led vermelho asceso direto
                #fica verde so um pouco pra indicar autenticacao
                #fora isso e vermelho direto
                # resultVerificacao vale None
                # entao nao ganha o 1 de verdade ref a verificacao
                
        # Apos verificar se a verificacao no banco...
        # A passagem do cartao he registrada, tenho sido a pessoa autorizada
        # ou seja, identificada corretamente
        # ou nao.

        dbCmd.insert_into_registro(objRegistro)
        ledCmd.apaga_led_verde()
        ledCmd.ascende_led_vermelho()    
    #aguarda o tempo de leitura pra voltar a consultar o serial do arduino    
    #print(datetime.datetime.now())
    #time.sleep(tempo_de_releitura_do_serial_do_arduino)

