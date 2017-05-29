import pymysql

mariadbServer='localhost'
mariadbUser='root'
mariadbPasswd=None
mariadbDb='catracas'


conn = pymysql.connect(
             host=mariadbServer,
             # unix_socket='/tmp/mysql.sock',
             user=mariadbUser,
             passwd=mariadbPasswd,
             db=mariadbDb)




# https://www.youtube.com/watch?v=o-vsdfCBpsU&list=PLQVvvaa0QuDezJh0sC5CqXLKZTSKU1YNo
def create_tables_if_not_exists():
    c = conn.cursor()    
    c.execute('CREATE TABLE IF NOT EXISTS registros (dev_id int ,momento datetime, id_card varchar(50), autorizado int, transferido_em datetime);')
    c.execute('CREATE TABLE IF NOT EXISTS cadastro_pessoas (nome varchar(250), matricula int, id_card varchar(50));')    
    # c.execute('CREATE UNIQUE INDEX IF NOT EXISTS rmUniqIdx ON cadastro_pessoas (matricula);')
    # c.execute("INSERT INTO cadastro_pessoas (nome,matricula,id_card) values ('nomeTeste',123,'124Teste')")
    c.close()

    
def insert_into_registro(registro):
    c = conn.cursor()
    str_momento = str(registro.momento)
    str_id_card = str(registro.id_card)
    num_autorizado = registro.autorizado
    trans_em = str(registro.transf_em)
    reg = [(str_momento, str_id_card, num_autorizado, trans_em)]
    sqlInsert = "INSERT INTO registros (momento,id_card,autorizado,transferido_em) values (?,?,?,?)"
    c.executemany(sqlInsert, reg)
    conn.commit()
    c.close()


