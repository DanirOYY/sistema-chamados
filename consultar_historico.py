
from pymongo import MongoClient

# Conectar ao MongoDB
cliente = MongoClient("mongodb://localhost:27017/")

# Selecionar banco e coleção
banco = cliente["historico_chamados"]
movimentacoes = banco["movimentacoes"]

# Consultar todos os históricos
print("HISTORICO DOS CHAMADOS")
print("----------------------")

for registro in movimentacoes.find().sort("data", 1):

    print("Chamado:", registro["chamado_id"])
    print("Data:", registro["data"])
    print("Responsavel:", registro["responsavel"])
    print("Acao:", registro["acao"])
    print("Observacoes:", registro["observacoes"])
    print("----------------------")

cliente.close()