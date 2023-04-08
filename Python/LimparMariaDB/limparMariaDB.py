import mysql.connector


def limpar_tabelas(usuario, senha, endereco, banco):
    # Connect com o banco MariaDB
    cnx = mysql.connector.connect(
        user=usuario, password=senha, host=endereco, database=banco)
    cursor = cnx.cursor()

    # Busca todas as tabelas do Banco
    query = (
        "SELECT table_name FROM information_schema.tables WHERE table_schema = %s")
    cursor.execute(query, (banco,))

    # Executa um Delete em cada uma das tabelas
    tables = cursor.fetchall()
    for table in tables:
        table_name = table[0]
        delete_query = f"DELETE FROM {table_name}"
        cursor.execute(delete_query)
        print(f"Dados da tabela {table_name} apagados")

    # Commita as alterações
    cnx.commit()
    cursor.close()
    cnx.close()
    input("Pressione Enter para fechar o terminal...")


# configurar a conexão
usuario = input("Informe o usuario do Banco: ")
senha = input("Informe a senha do Banco: ")
endereco = input("Informe o endereço do Banco: ")
banco = input("Informe o nome do Banco: ")

limpar_tabelas(usuario, senha, endereco, banco)
