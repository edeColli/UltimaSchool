import sqlite3

conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()

sql = '''
  CREATE TABLE categoria (
	Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Descricao TEXT(100)
);
'''
try:
    cursor.execute(sql)
    conexao.commit()
except:
    print('Não foi possível criar a tabela!')
    conexao.rollback()

conexao.close()
