
import sqlite3

# Conectar ao banco
conexao = sqlite3.connect("chamados.db")
cursor = conexao.cursor()

print("===== CONSULTAR CHAMADO =====")

# Pedir o numero do chamado
chamado_id = int(input("Digite o ID do chamado: "))

# Buscar os dados nas tres tabelas
cursor.execute("""
SELECT
    chamados.id,
    usuarios.nome,
    usuarios.email,
    categorias.nome,
    chamados.equipamento,
    chamados.descricao,
    chamados.status,
    chamados.data_criacao

FROM chamados

LEFT JOIN usuarios
ON chamados.solicitante_id = usuarios.id

LEFT JOIN categorias
ON chamados.categoria_id = categorias.id

WHERE chamados.id = ?
""", (chamado_id,))

chamado = cursor.fetchone()

if chamado:

    print("\n===== DETALHES DO CHAMADO =====")

    print("ID:", chamado[0])
    print("Solicitante:", chamado[1])
    print("Email:", chamado[2])
    print("Categoria:", chamado[3])
    print("Equipamento:", chamado[4])
    print("Descricao:", chamado[5])
    print("Status:", chamado[6])
    print("Data de criacao:", chamado[7])

else:
    print("Chamado nao encontrado!")

conexao.close()
