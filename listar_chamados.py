
import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect("chamados.db")
cursor = conexao.cursor()

# Consultar todos os chamados
cursor.execute("""
SELECT * FROM chamados
""")

chamados = cursor.fetchall()

print("\n===== LISTA DE CHAMADOS =====\n")

if chamados:

    for chamado in chamados:

        print("ID:", chamado[0])
        print("Solicitante:", chamado[1])
        print("Categoria:", chamado[2])
        print("Equipamento:", chamado[3])
        print("Descricao:", chamado[4])
        print("----------------------------")

else:
    print("Nenhum chamado encontrado.")

conexao.close()