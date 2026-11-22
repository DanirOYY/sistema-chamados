# Sistema de Chamados

## Sobre o projeto

Este projeto consiste em um sistema de gerenciamento de chamados de suporte técnico, desenvolvido em Python, utilizando banco de dados SQLite e MongoDB.

O sistema permite registrar, consultar e acompanhar chamados técnicos, além de armazenar o histórico de movimentações.

## Tecnologias utilizadas

- Python
- SQLite
- MongoDB
- PyMongo
- Tkinter

## Funcionalidades

- Cadastro de chamados.
- Listagem de chamados.
- Consulta de detalhes dos chamados.
- Alteração de status.
- Adição de comentários.
- Consulta do histórico de movimentações.
- Integração entre SQLite e MongoDB.
- Interface gráfica para visualizar os chamados.

## Banco de dados

**SQLite:** armazena os usuários, categorias e chamados.

**MongoDB:** armazena o histórico de movimentações e comentários dos chamados.

## Arquivos do projeto

Os arquivos Python estão organizados por funcionalidade, incluindo conexão com os bancos de dados, criação, consulta e atualização de chamados.

## Como executar

1. Instale o Python.
2. Instale o PyMongo com o comando:

   `pip install pymongo`

3. Certifique-se de que o MongoDB esteja instalado e em execução.
4. Abra a pasta do projeto no VS Code.
5. Execute o arquivo `interface.py` para abrir a interface gráfica.

## Autor

Projeto desenvolvido como atividade acadêmica.
