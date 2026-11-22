
import sqlite3
from pymongo import MongoClient
from datetime import datetime

# 1. Conectar ao SQLite
conexao = sqlite3.connect("chamados.db")
cursor = conexao.cursor()

# 2. Procurar o usuario
cursor.execute("""
SELECT id FROM usuarios
WHERE email = 'joao@email.com'
""")

usuario = cursor.fetchone()

# 3. Procurar a categoria
cursor.execute("""
SELECT id FROM categorias
WHERE nome = 'Hardware'
""")

categoria = cursor.fetchone()

if usuario and categoria:

    # 4. Criar chamado no SQLite
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
        "Notebook",
        "O notebook está muito lento."
    ))

    # Descobrir o numero do chamado criado
    chamado_id = cursor.lastrowid

    conexao.commit()

    print("Chamado criado no SQLite!")

    # 5. Conectar ao MongoDB
    cliente = MongoClient("mongodb://localhost:27017/")
    banco = cliente["historico_chamados"]
    movimentacoes = banco["movimentacoes"]

    # 6. Registrar a criacao no historico
    movimentacoes.insert_one({
        "chamado_id": chamado_id,
        "data": datetime.now(),
        "responsavel": "Sistema",
        "acao": "Chamado criado",
        "observacoes": "Chamado registrado no sistema."
    })

    print("Historico registrado no MongoDB!")
    print("Numero do chamado:", chamado_id)

    cliente.close()

else:
    print("Usuario ou categoria nao encontrados.")

conexao.close()