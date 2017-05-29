import pandas
import sqlite3

conn = sqlite3.connect('catracas.db')
df = pandas.read_csv("load_cadastro_pessoas.csv", sep=";")
df.to_sql("cadastro_pessoas", conn, if_exists='append', index=False)
# ,index_label="nome,matricula,id_card")
