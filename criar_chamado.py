
import sqlite3

conexao = sqlite3.connect("chamados.db")
cursor = conexao.cursor()

# Procurar o usuário João
cursor.execute("""
SELECT id FROM usuarios
WHERE email = 'joao@email.com'
""")

usuario = cursor.fetchone()

# Procurar a categoria Hardware
cursor.execute("""
SELECT id FROM categorias
WHERE nome = 'Hardware'
""")

categoria = cursor.fetchone()

# Criar o chamado
if usuario and categoria:
    cursor.execute("""
    INSERT INTO chamados (
        solicitante_id,
        categoria_id,
        equipamento,
        descricao
    )
    VALUES (?, ?, ?, ?)
    """, (
        usuario[0],
        categoria[0],
        "Computador",
        "Meu computador não está ligando."
    ))

    conexao.commit()
    print("Chamado cadastrado com sucesso!")

else:
    print("Usuário ou categoria não encontrados.")

conexao.close()