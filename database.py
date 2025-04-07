import pandas as pd
from cryp import criptografar_senha, descriptografar_senha

def consulta_todos_usuarios():
    df = pd.read_excel('db.xlsx', sheet_name='usuarios')
    return df

def consulta_id(id):
    df = pd.read_excel('db.xlsx', sheet_name='usuarios')
    usuario = df[df['id'] == id]
    if not usuario.empty:
        return usuario
    else:
        return 'Usuário não encontrado!'

def criar_usuario(id, nome, conta, senha, nivel='usuario'):
    try:
        df = pd.read_excel('db.xlsx', sheet_name='usuarios')
    except:
        df = pd.DataFrame(columns=['id', 'nome', 'conta', 'senha', 'nivel'])

    senha_cifrada = criptografar_senha(senha)
    novo_usuario = {
        'id': id,
        'nome': nome,
        'conta': conta,
        'senha': senha_cifrada,
        'nivel': nivel
    }

    df = pd.concat([df, pd.DataFrame([novo_usuario])], ignore_index=True)

    with pd.ExcelWriter('db.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='usuarios', index=False)

    saldo_df = pd.read_excel('db.xlsx', sheet_name='saldo')
    novo_saldo = {'id': id, 'saldo': 1000.00}
    saldo_df = pd.concat([saldo_df, pd.DataFrame([novo_saldo])], ignore_index=True)
    with pd.ExcelWriter('db.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        saldo_df.to_excel(writer, sheet_name='saldo', index=False)

def deletar_usuario(id):
    df = pd.read_excel('db.xlsx', sheet_name='usuarios')
    df = df[df['id'] != id]
    with pd.ExcelWriter('db.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        df.to_excel(writer, sheet_name='usuarios', index=False)

def deletar_todos_usuarios():
    df = pd.DataFrame(columns=['id', 'nome', 'conta', 'senha', 'nivel'])
    with pd.ExcelWriter('db.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='usuarios', index=False)

def autenticar(conta, senha_digitada):
    try:
        df = pd.read_excel('db.xlsx', sheet_name='usuarios')
    except:
        return None

    usuario = df[df['conta'] == conta]
    if not usuario.empty:
        senha_cifrada = usuario.iloc[0]['senha']
        try:
            senha_original = descriptografar_senha(senha_cifrada)
            if senha_digitada == senha_original:
                return usuario.iloc[0].to_dict()
        except Exception as e:
            print("Erro ao descriptografar senha:", e)
            return None
    return None

