
import sqlite3

# Abrir o banco de dados
conexao = sqlite3.connect("chamados.db")
cursor = conexao.cursor()

# Cadastrar usuários
cursor.execute("""
INSERT OR IGNORE INTO usuarios (nome, email)
VALUES ('João Silva', 'joao@email.com')
""")

cursor.execute("""
INSERT OR IGNORE INTO usuarios (nome, email)
VALUES ('Maria Santos', 'maria@email.com')
""")

# Cadastrar categorias
categorias = [
    ("Hardware",),
    ("Software",),
    ("Rede",),
    ("Impressora",)
]

cursor.executemany("""
INSERT OR IGNORE INTO categorias (nome)
VALUES (?)
""", categorias)

# Salvar os dados
conexao.commit()

print("Cadastros realizados com sucesso!")

# Mostrar usuários cadastrados
print("\nUSUÁRIOS:")
cursor.execute("SELECT * FROM usuarios")

for usuario in cursor.fetchall():
    print(usuario)

# Mostrar categorias cadastradas
print("\nCATEGORIAS:")
cursor.execute("SELECT * FROM categorias")

for categoria in cursor.fetchall():
    print(categoria)

conexao.close()