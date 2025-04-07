#pip install -r requirements.txt

from database import criar_usuario, autenticar, deletar_usuario, deletar_todos_usuarios
from database import consulta_todos_usuarios, consulta_id
from transactions import consulta_saldo, saque, deposito, transferencia
from cryp import gerar_chave
from colorama import Fore, Style, init
init(autoreset=True)
import os

if not os.path.exists("chave.key"):
    gerar_chave()

def menu_admin(usuario):
    while True:
        print("\n" + "-"*40)
        print(f"🛡️ Painel Admin: {usuario['nome']}")
        print("1. 📊 Consultar saldo de um usuário")
        print("2. 📋 Consultar todos os usuários")
        print("3. 🗑️ Deletar usuário por ID")
        print("4. ⚠️ Deletar TODOS os usuários")
        print("0. ↩️ Sair")
        op = input("Escolha: ")

        if op == "1":
            id = int(input("ID do usuário: "))
            print(consulta_saldo(id))

        elif op == "2":
            print(consulta_todos_usuarios())

        elif op == "3":
            id = int(input("ID do usuário a deletar: "))
            deletar_usuario(id)
            print("✅ Usuário deletado.")

        elif op == "4":
            confirm = input("Tem certeza que deseja deletar todos os usuários? (s/n): ")
            if confirm.lower() == 's':
                deletar_todos_usuarios()
                print("⚠️ Todos os usuários foram deletados.")

        elif op == "0":
            break

def menu_usuario(usuario):
    while True:
        print("\n" + Fore.BLUE + "-"*40)
        print(Fore.YELLOW + f"👤 Bem-vindo, {usuario['nome']}")
        print(Fore.GREEN + "1. 📊 Consultar saldo")
        print("2. 💸 Saque")
        print("3. 💰 Depósito")
        print("4. 🔄 Transferência")
        print("0. ↩️ Sair")
        op = input(Fore.CYAN + "Escolha: ")

        if op == "1":
            print(Fore.YELLOW + consulta_saldo(usuario['id']))
        elif op == "2":
            valor = float(input(Fore.CYAN + "Valor do saque: R$ "))
            print(Fore.YELLOW + saque(usuario['id'], valor))
        elif op == "3":
            valor = float(input(Fore.CYAN + "Valor do depósito: R$ "))
            print(Fore.YELLOW + deposito(usuario['id'], valor))
        elif op == "4":
            id_destino = int(input(Fore.CYAN + "ID do destinatário: "))
            valor = float(input(Fore.CYAN + "Valor da transferência: R$ "))
            print(Fore.YELLOW + transferencia(usuario['id'], id_destino, valor))
        elif op == "0":
            break


def criar_conta():
    id = int(input("ID: "))
    nome = input("Nome: ")
    conta = input("Conta (usuário): ")
    senha = input("Senha: ")
    nivel = input("Nível (admin ou usuario): ").lower()
    criar_usuario(id, nome, conta, senha, nivel)
    print("Conta criada com sucesso!")

def login():
    conta = input("Conta: ")
    senha = input("Senha: ")
    usuario = autenticar(conta, senha)
    if usuario:
        if usuario['nivel'] == 'admin':
            menu_admin(usuario)
        else:
            menu_usuario(usuario)
    else:
        print("Login inválido.")

def inicio():
    while True:
        print("\n" + Fore.CYAN + "="*30)
        print(Fore.YELLOW + "      🌟 BANCO PYTHON 🌟")
        print(Fore.CYAN + "="*30)
        print(Fore.GREEN + "1. 📝 Criar conta")
        print("2. 🔐 Fazer login")
        print("0. ❌ Sair")
        escolha = input(Fore.BLUE + "Escolha uma opção: " + Style.RESET_ALL)
        
        if escolha == "1":
            criar_conta()
        elif escolha == "2":
            login()
        elif escolha == "0":
            print(Fore.MAGENTA + "Saindo... Até logo!")
            break
        else:
            print(Fore.RED + "🚫 Opção inválida.")

inicio()
