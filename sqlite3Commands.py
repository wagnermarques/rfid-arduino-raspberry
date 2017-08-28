import sqlite3


conn = sqlite3.connect('catracas.db')


# https://www.youtube.com/watch?v=o-vsdfCBpsU&list=PLQVvvaa0QuDezJh0sC5CqXLKZTSKU1YNo
def create_table():
    c = conn.cursor()
    sqlCreateRegistroTable = ('CREATE TABLE IF NOT EXISTS registros ('+
    'dev_id int ,'+
    'momento TEXT, '+
    'id_card TEXT, '+
    'autorizado INTEGER,'+ 
    'id_pessoa_autorizada int, '+
    'transferido_em TEXT)')
    
    c.execute(sqlCreateRegistroTable)
    c.execute('CREATE TABLE IF NOT EXISTS cadastro_pessoas (nome TEXT, matricula INTEGER, id_card TEXT);')    
    c.execute('CREATE UNIQUE INDEX IF NOT EXISTS rmUniqIdx ON cadastro_pessoas (matricula);')
    # c.execute("INSERT INTO cadastro_pessoas (nome,matricula,id_card) values ('nomeTeste',123,'124Teste')")
    c.close()

    
def insert_into_registro(registro):
    c = conn.cursor()
    str_momento = str(registro.momento)
    str_id_card = str(registro.id_card)
    num_autorizado = registro.autorizado
    id_pessoa_autorizada = registro.id_pessoa_identificada
    reg = [(str_momento, str_id_card, num_autorizado,id_pessoa_autorizada)]

    sqlInsert = "INSERT INTO registros (momento,id_card,autorizado,id_pessoa_autorizada) values (?,?,?,?)"
    c.executemany(sqlInsert, reg)
    conn.commit()
    c.close()


    
def insert_into_pessoa(pessoa):
    c = conn.cursor()
    str_momento = str(registro.momento)
    str_id_card = str(registro.id_card)
    num_autorizado = registro.autorizado
    reg = [(str_momento, str_id_card, num_autorizado)]

    sqlInsert = "INSERT INTO registros (momento,id_card,autorizado) values (?,?,?)"
    c.executemany(sqlInsert, reg)
    conn.commit()
    c.close()
    
    

def verifica_pessoa_cadastrada_by_id_card(id_card):

    str_id_card = str(id_card)

    c = conn.cursor()
    sqlInsert = "SELECT nome, matricula, id_card FROM cadastro_pessoas where id_card = '" + str_id_card + "';"
    print(sqlInsert)
    resultCursor = c.execute(sqlInsert)

    resultList = resultCursor.fetchall()

    if(len(resultList) == 0):
        return None

    if (len(resultList) == 1):
        row = resultList[0]
        pessNome = row[0]
        # objPessVerificada = Pessoa(
        return resultList[0]

    if (len(resultList) > 1):
        return None



def select_registros_nao_transferidos():
    c = conn.cursor()
    sql = "SELECT * FROM registros where transferido_em is NULL"
    c.execute(sql)
    all = c.fetchall()
    c.close()
    return all
    
