
import sqlite3
from pymongo import MongoClient
from datetime import datetime

# 1. Conectar ao SQLite
conexao = sqlite3.connect("chamados.db")
cursor = conexao.cursor()

# 2. Escolher o chamado que queremos alterar
chamado_id = 2

# 3. Verificar se o chamado existe
cursor.execute(
    "SELECT id, status FROM chamados WHERE id = ?",
    (chamado_id,)
)

chamado = cursor.fetchone()

if chamado:

    status_antigo = chamado[1]
    novo_status = "Em andamento"

    # 4. Atualizar o status no SQLite
    cursor.execute("""
    UPDATE chamados
    SET status = ?
    WHERE id = ?
    """, (novo_status, chamado_id))

    conexao.commit()

    print("Status atualizado no SQLite!")

    # 5. Conectar ao MongoDB
    cliente = MongoClient("mongodb://localhost:27017/")

    banco = cliente["historico_chamados"]
    movimentacoes = banco["movimentacoes"]

    # 6. Registrar a alteração no histórico
    movimentacoes.insert_one({
        "chamado_id": chamado_id,
        "data": datetime.now(),
        "responsavel": "Sistema",
        "acao": "Status alterado",
        "observacoes": (
            "Status alterado de "
            + status_antigo
            + " para "
            + novo_status
        )
    })

    print("Alteração registrada no MongoDB!")
    print("Status anterior:", status_antigo)
    print("Novo status:", novo_status)

    cliente.close()

else:
    print("Chamado não encontrado!")

conexao.close()