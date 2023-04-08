def executarSql(conexao, sql):
    cursor = conexao.cursor()
    try:
        cursor.execute(sql)
        conexao.commit()
    except:
        print('Não foi possível executar o comando SQL!')
        conexao.rollback()
