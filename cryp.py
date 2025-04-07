from cryptography.fernet import Fernet
import os

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)

def carregar_chave():
    return open("chave.key", "rb").read()

if not os.path.exists("chave.key"):
    gerar_chave()

chave = carregar_chave()
fernet = Fernet(chave)

def criptografar_senha(senha):
    return fernet.encrypt(senha.encode()).decode()

def descriptografar_senha(senha_cifrada):
    return fernet.decrypt(senha_cifrada.encode()).decode()
