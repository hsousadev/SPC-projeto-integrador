import pandas as pd
from data import fatec_operacao, fonte, indice_fontes


def valida_fonte():
    fontes_sem_indentificação = list()
    for id_fonte in indice_fontes:
        if id_fonte not in list(fonte["id_fonte"]):
            fontes_sem_indentificação.append(id_fonte)
    porcentagem = (len(fontes_sem_indentificação) / fonte.shape[0]) * 100
    return porcentagem, fontes_sem_indentificação


def validaCpf(cpf, d1=0, d2=0, i=0):

    while i<10:
        d1,d2,i=(d1+(int(cpf[i])*(11-i-1)))%11 if i<9 else d1,(d2+(int(cpf[i])*(11-i)))%11,i+1
    return (int(cpf[9])==(11-d1 if d1>1 else 0)) and (int(cpf[10])==(11-d2 if d2>1 else 0))


def validaCnpj(cnpj):
    str(cnpj)

    if (not cnpj) or (len(cnpj) < 14):
        return False

    # Pega apenas os 12 primeiros dígitos do CNPJ e gera os 2 dígitos que faltam
    inteiros = list(map(int, cnpj))
    novo = inteiros[:12]

    mascara_validacao = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2] # Fornecida pela receita federal
    while len(novo) < 14:
        r = sum([x*y for (x, y) in zip(novo, mascara_validacao)]) % 11
        if r > 1:
            f = 11 - r
        else:
            f = 0
        novo.append(f)
        mascara_validacao.insert(0, 6)

    # Se o número gerado coincidir com o número original, é válido
    if novo == inteiros:
        return True
    return False


def cpfInvalidos(fonte):
    cpf_invalidos = list()
    cnpj_invalidos = list()
    doc_fonte = fatec_operacao[(fatec_operacao["id_fnt"] == fonte)]
    listDoc = [list(doc_fonte["doc_cli"]), list(doc_fonte["tip_cli"])]
    
    for index in range(len(listDoc)):
        if listDoc[1][index] == "F":
            if not validaCpf(listDoc[0][index]):
                cpf_invalidos.append(listDoc[0][index])
        
        else:
            if not validaCnpj(listDoc[0][index]):
                cnpj_invalidos.append(listDoc[0][index])
    

    porcentagem = ((len(cpf_invalidos) + len(cnpj_invalidos)) / len(listDoc)) * 100
    return porcentagem, cpf_invalidos, cnpj_invalidos


def validaNumerico(df, coluna):
    contInvalidos = int()
    camposInvalidos = list()
    
    for campo in df[coluna]:
        try:
            float(campo)
            
        except ValueError:
            if campo != 'NULL':
                contInvalidos += 1
                camposInvalidos.append(campo)
                
    try:
        porcentagem = (1 - (len(coluna) / contInvalidos)) * 100
    
    except ZeroDivisionError:
        porcentagem = 100
        
    return porcentagem, camposInvalidos
