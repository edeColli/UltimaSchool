sql_organizador = '''CREATE TABLE if not exists organizador (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(50) NOT NULL,
  email VARCHAR(50),
	CPF VARCHAR(15)
)'''

sql_evento = '''CREATE TABLE if not exists evento (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	titulo VARCHAR(100),
  data VARHCAR(10),
  local VARCHAR(100)
)'''

sql_organizador_evento = '''CREATE TABLE if not exists organizador_evento (
  id_organizador INTEGER,
	id_evento INTEGER,
	CONSTRAINT organizador_evento_FK FOREIGN KEY (id_organizador) REFERENCES organizador(id),
	CONSTRAINT organizador_evento_FK_1 FOREIGN KEY (id_evento) REFERENCES evento(id)
)'''


def sql():
    return [sql_organizador, sql_evento, sql_organizador_evento]
