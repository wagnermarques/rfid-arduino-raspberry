import sys

import sqlite3Commands as sqliteCmd
import mariadbCommands as mariaCmd
import model       

mariaCmd.create_tables_if_not_exists();

# Este metodo transfere todos os registros do sqlite
# para o mariadb, que sera um banco central de todos os sqlites
# mas transfere apenas os registros que ainda nao tiverem sido transferidos
# no sqlite, registros tranferidos tem seu campo "trasnferido_em" com o timestamp do momento que foi confirmado sua transferencia.
# esse timestamp de transferido realizado por este metodo
# os registros do sqlite que tiverem timestamp definidos no campo
# transferido_em nao sao mais transferidos
def transfere_registros_sqlite_to_mariadb():    
    allRegsToTransfer = sqliteCmd.select_registros_nao_transferidos();
    for linha in allRegsToTransfer:
        strMomento=str(linha[1])
        strIdCard=str(linha[2])
        intAutorizado=linha[3]
        strTransfEm=str(linha[4])
        print(strMomento)
        print(strIdCard)
        print(intAutorizado)
        print(strTransfEm)
        
        registro = model.Registro(strMomento,strIdCard,intAutorizado,strTransfEm)

        print("registro.momento:"+ registro.momento)
        print("registro.id_card:" +registro.id_card)
        print("registro.autorizado:" +str(registro.autorizado))
        print("registro.transf_em:" +registro.transf_em)
        
        try:
            mariaCmd.insert_into_registro(registro)
        except:
            print(sys.exc_info()[0])
            raise
        
        
transfere_registros_sqlite_to_mariadb()
