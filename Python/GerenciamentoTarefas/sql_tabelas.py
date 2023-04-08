sql_categoria = '''CREATE TABLE if not exists categoria (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT(50)
)'''

sql_status = '''CREATE TABLE if not exists status (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	descricao TEXT(20)
)'''

sql_tarefa = '''CREATE TABLE if not exists tarefa(
  id INTEGER not null primary key autoincrement,
  nome TEXT(50) not null,
  data TEXT(10),
  categoria_id integer,
  status_id integer,
  CONSTRAINT tarefa_categoria_FK FOREIGN KEY (categoria_id) REFERENCES categoria1(id) ON DELETE RESTRICT,
	CONSTRAINT tarefa_status_FK FOREIGN KEY (status_id) REFERENCES status(id) ON DELETE RESTRICT
)'''

sql_historico_execucao_tarefa = '''CREATE TABLE if not exists historico_execucao_tarefa (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tarefa_id INTEGER,
	status_id INTEGER,
	"data" TEXT(10),
	CONSTRAINT historico_execucao_tarefa_FK FOREIGN KEY (status_id) REFERENCES status(id),
	CONSTRAINT historico_execucao_tarefa_FK_1 FOREIGN KEY (tarefa_id) REFERENCES tarefa(id)
)'''


def sql():
    return [sql_categoria, sql_status, sql_tarefa, sql_historico_execucao_tarefa]
