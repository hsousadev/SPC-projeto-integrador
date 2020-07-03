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

def validaCnpj():
    pass


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
    return porcentagem, cpf_invalidos





