import pandas as pd

def consulta_saldo(id):
    df = pd.read_excel('db.xlsx', sheet_name='saldo')
    usuario = df[df['id'] == id]
    if not usuario.empty:
        saldo = usuario.iloc[0]['saldo']
        return f"Seu saldo é de R$ {saldo:.2f}"
    else:
        return 'Usuário não encontrado!'

def altera_saldo(id, nova_coluna, novo_valor):
    df = pd.read_excel('db.xlsx', sheet_name='saldo')
    if id in df['id'].values:
        df.loc[df['id'] == id, nova_coluna] = novo_valor
        with pd.ExcelWriter('db.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, sheet_name='saldo', index=False)
        return f'Dado alterado com sucesso para o usuário {id}.'
    else:
        return 'Usuário não encontrado!'

def saque(id, valor):
    df = pd.read_excel('db.xlsx', sheet_name='saldo')
    if id in df['id'].values:
        saldo_atual = df.loc[df['id'] == id, 'saldo'].values[0]
        if saldo_atual >= valor:
            df.loc[df['id'] == id, 'saldo'] = saldo_atual - valor
            with pd.ExcelWriter('db.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                df.to_excel(writer, sheet_name='saldo', index=False)
            return f"Saque de R$ {valor:.2f} realizado com sucesso!"
        else:
            return "Saldo insuficiente."
    return "Usuário não encontrado."

def deposito(id, valor):
    df = pd.read_excel('db.xlsx', sheet_name='saldo')
    if id in df['id'].values:
        df.loc[df['id'] == id, 'saldo'] += valor
        with pd.ExcelWriter('db.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, sheet_name='saldo', index=False)
        return f"Depósito de R$ {valor:.2f} realizado com sucesso!"
    return "Usuário não encontrado."

def transferencia(id_origem, id_destino, valor):
    df = pd.read_excel('db.xlsx', sheet_name='saldo')
    if id_origem in df['id'].values and id_destino in df['id'].values:
        saldo_origem = df.loc[df['id'] == id_origem, 'saldo'].values[0]
        if saldo_origem >= valor:
            df.loc[df['id'] == id_origem, 'saldo'] -= valor
            df.loc[df['id'] == id_destino, 'saldo'] += valor
            with pd.ExcelWriter('db.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                df.to_excel(writer, sheet_name='saldo', index=False)
            return f"Transferência de R$ {valor:.2f} concluída."
        else:
            return "Saldo insuficiente para a transferência."
    return "Usuário(s) não encontrado(s)."
