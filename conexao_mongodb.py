
from pymongo import MongoClient

# Conectar ao MongoDB
cliente = MongoClient("mongodb://localhost:27017/")

# Selecionar nosso banco
banco = cliente["historico_chamados"]

# Selecionar nossa coleção
movimentacoes = banco["movimentacoes"]

# Testar a conexão
cliente.admin.command("ping")

print("Conexão com MongoDB realizada com sucesso!")

cliente.close()