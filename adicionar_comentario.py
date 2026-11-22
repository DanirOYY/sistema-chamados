
import sqlite3
from pymongo import MongoClient
from datetime import datetime

# 1. Conectar ao banco SQL
conexao = sqlite3.connect("chamados.db")
cursor = conexao.cursor()

# 2. Pedir o numero do chamado
chamado_id = int(input("Digite o numero do chamado: "))

# 3. Verificar se o chamado existe
cursor.execute(
    "SELECT id FROM chamados WHERE id = ?",
    (chamado_id,)
)

chamado = cursor.fetchone()

if chamado:

    # 4. Pedir as informacoes do comentario
    responsavel = input("Digite seu nome: ")
    comentario = input("Digite seu comentario: ")

    # 5. Conectar ao MongoDB
    cliente = MongoClient("mongodb://localhost:27017/")

    banco = cliente["historico_chamados"]
    movimentacoes = banco["movimentacoes"]

    # 6. Salvar o comentario no historico
    movimentacoes.insert_one({
        "chamado_id": chamado_id,
        "data": datetime.now(),
        "responsavel": responsavel,
        "acao": "Comentario adicionado",
        "observacoes": comentario
    })

    print("\nComentario registrado com sucesso!")

    cliente.close()

else:
    print("Chamado nao encontrado!")

# 7. Fechar conexao SQL
conexao.close()