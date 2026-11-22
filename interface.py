
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

janela = tk.Tk()
janela.title("Sistema de Chamados")
janela.geometry("900x550")


def carregar_chamados():

    for item in tabela.get_children():
        tabela.delete(item)

    conexao = sqlite3.connect("chamados.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            chamados.id,
            usuarios.nome,
            categorias.nome,
            chamados.equipamento,
            chamados.status
        FROM chamados
        LEFT JOIN usuarios
        ON chamados.solicitante_id = usuarios.id
        LEFT JOIN categorias
        ON chamados.categoria_id = categorias.id
    """)

    for chamado in cursor.fetchall():
        tabela.insert("", "end", values=chamado)

    conexao.close()


def ver_detalhes():

    selecionado = tabela.selection()

    if not selecionado:
        messagebox.showwarning("Atenção", "Selecione um chamado!")
        return

    dados = tabela.item(selecionado[0])
    chamado_id = dados["values"][0]

    conexao = sqlite3.connect("chamados.db")
    cursor = conexao.cursor()

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
    conexao.close()

    if chamado:
        detalhes = (
            f"ID: {chamado[0]}\n"
            f"Solicitante: {chamado[1]}\n"
            f"Email: {chamado[2]}\n"
            f"Categoria: {chamado[3]}\n"
            f"Equipamento: {chamado[4]}\n"
            f"Descrição: {chamado[5]}\n"
            f"Status: {chamado[6]}\n"
            f"Data de criação: {chamado[7]}"
        )

        messagebox.showinfo("Detalhes do Chamado", detalhes)


def novo_chamado():

    cadastro = tk.Toplevel(janela)
    cadastro.title("Novo Chamado")
    cadastro.geometry("400x400")

    tk.Label(cadastro, text="NOVO CHAMADO",
             font=("Arial", 16, "bold")).pack(pady=15)

    tk.Label(cadastro, text="Solicitante:").pack()
    conexao = sqlite3.connect("chamados.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome FROM usuarios")
    usuarios = cursor.fetchall()

    cursor.execute("SELECT id, nome FROM categorias")
    categorias = cursor.fetchall()

    conexao.close()

    mapa_usuarios = {nome: id for id, nome in usuarios}
    mapa_categorias = {nome: id for id, nome in categorias}

    campo_usuario = ttk.Combobox(
        cadastro,
        values=list(mapa_usuarios.keys()),
        state="readonly"
    )
    campo_usuario.pack(pady=5)

    tk.Label(cadastro, text="Categoria:").pack()
    campo_categoria = ttk.Combobox(
        cadastro,
        values=list(mapa_categorias.keys()),
        state="readonly"
    )
    campo_categoria.pack(pady=5)

    tk.Label(cadastro, text="Equipamento:").pack()
    campo_equipamento = tk.Entry(cadastro, width=35)
    campo_equipamento.pack(pady=5)

    tk.Label(cadastro, text="Descrição:").pack()
    campo_descricao = tk.Entry(cadastro, width=35)
    campo_descricao.pack(pady=5)

    def salvar_chamado():

        usuario = campo_usuario.get()
        categoria = campo_categoria.get()
        equipamento = campo_equipamento.get().strip()
        descricao = campo_descricao.get().strip()

        if not usuario or not categoria or not equipamento or not descricao:
            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos!"
            )
            return

        conexao = sqlite3.connect("chamados.db")
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO chamados
            (solicitante_id, categoria_id, equipamento, descricao)
            VALUES (?, ?, ?, ?)
        """, (
            mapa_usuarios[usuario],
            mapa_categorias[categoria],
            equipamento,
            descricao
        ))

        conexao.commit()
        conexao.close()

        messagebox.showinfo(
            "Sucesso",
            "Chamado cadastrado com sucesso!"
        )

        cadastro.destroy()
        carregar_chamados()

    tk.Button(
        cadastro,
        text="Salvar chamado",
        command=salvar_chamado
    ).pack(pady=20)


# Interface principal

titulo = tk.Label(
    janela,
    text="SISTEMA DE CHAMADOS",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=20)

colunas = ("ID", "Solicitante", "Categoria", "Equipamento", "Status")

tabela = ttk.Treeview(
    janela,
    columns=colunas,
    show="headings"
)

for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column(coluna, width=160)

tabela.pack(fill="both", expand=True, padx=20, pady=10)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=15)

tk.Button(
    frame_botoes,
    text="Atualizar chamados",
    command=carregar_chamados
).pack(side="left", padx=10)

tk.Button(
    frame_botoes,
    text="Ver detalhes",
    command=ver_detalhes
).pack(side="left", padx=10)

tk.Button(
    frame_botoes,
    text="Novo chamado",
    command=novo_chamado
).pack(side="left", padx=10)

carregar_chamados()

janela.mainloop()