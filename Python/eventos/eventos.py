import sql_tabelas
import sqlite3
import comandoSQL

conexao = sqlite3.connect('eventos.sqlite3')

for sql in sql_tabelas.sql():
    comandoSQL.executarSql(conexao, sql)
