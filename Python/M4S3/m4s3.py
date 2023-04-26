import sqlite3
import requests
from bs4 import BeautifulSoup

# Cria uma conexão com o banco de dados
conn = sqlite3.connect("noticias.db")

# Cria uma tabela para armazenar as notícias
conn.execute("""
    CREATE TABLE IF NOT EXISTS noticias (
        categoria TEXT,
        titulo TEXT,
        data TEXT,
        descricao TEXT
    )
""")

url = "http://raspagem.herokuapp.com/noticias/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

categorias = soup.find_all("div", class_="card-header")

for categoria in categorias:
    categoria_link = categoria.find("a")["href"]
    categoria_nome = categoria.find("h2").text

    print(f"Categoria: {categoria_nome}")
    print("")

    categoria_response = requests.get(categoria_link)
    categoria_soup = BeautifulSoup(categoria_response.content, "html.parser")

    noticias = categoria_soup.find_all("div", class_="col-sm-12 col-md-6 col-lg-4")

    for noticia in noticias:
        titulo = noticia.find("h3").text
        data = noticia.find("span", class_="date").text
        descricao = noticia.find("p").text

        # Insere as informações da notícia na tabela
        conn.execute("INSERT INTO noticias VALUES (?, ?, ?, ?)", (categoria_nome, titulo, data, descricao))
        conn.commit()

        print(f"Título: {titulo}")
        print(f"Data: {data}")
        print(f"Descrição: {descricao}")
        print("")

# Fecha a conexão com o banco de dados
conn.close()
