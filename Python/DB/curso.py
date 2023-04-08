import sqlite3

conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()

sql = 'Select * from usuario'

consulta = cursor.execute(sql)

for c in consulta:
    print(c)
