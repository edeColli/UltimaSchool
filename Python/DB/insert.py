import sqlite3

conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()

sql = '''INSERT into categoria (Descricao) values ('celulares')'''
try:
    cursor.execute(sql)
    conexao.commit()
except:
    print('Não foi possível inserir dados na tabela!')
    conexao.rollback()
