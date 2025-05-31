# Broadcast-Server - https://roadmap.sh/projects/broadcast-server

# 🛰️ Broadcast Server em Python

Este projeto é uma aplicação simples em Python que simula um **servidor de broadcast** em tempo real via WebSockets. Ele permite que múltiplos clientes se conectem, troquem mensagens e recebam atualizações instantaneamente — uma base excelente para sistemas como **chats, notificações em tempo real, placares, etc.**

## 🎯 Objetivo

Explorar o funcionamento da comunicação **cliente-servidor em tempo real**, utilizando `websockets` com `asyncio` para gerenciar múltiplas conexões simultâneas de forma eficiente.

---

## ⚙️ Tecnologias

- Python 3.9+
- [websockets](https://websockets.readthedocs.io/)
- asyncio
- argparse (interface de linha de comando)

---

## 🚀 Como rodar o projeto

### 1. Instale as dependências

bash
pip install websockets

2. Clone este repositório

git clone https://github.com/seu-usuario/broadcast-server-python.git
cd broadcast-server-python

3. Inicie o servidor

python main.py start
O servidor escutará conexões na porta 6789.

4. Inicie um ou mais clientes
Em outro terminal:


python main.py connect
Você poderá digitar mensagens e receber transmissões em tempo real.

💡 Exemplos
Abra um terminal e execute python main.py start

Abra outro(s) terminal(is) e execute python main.py connect

Envie mensagens de qualquer cliente: todos os conectados receberão

🧠 Conceitos aplicados
WebSocket bidirecional com websockets

Comunicação assíncrona com asyncio

CLI simples com argparse

Transmissão para múltiplos clientes (broadcast)

Gerenciamento de conexão/desconexão em tempo real

🛠️ Possíveis melhorias
Atribuir nomes ou apelidos aos clientes

Criar uma interface gráfica com Tkinter ou PyQt

Histórico de mensagens com salvamento em JSON

Implementar criptografia e autenticação

🐍 Autor
Feito com 💻 por Gabriel Torres
