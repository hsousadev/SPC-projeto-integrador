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
    while i < 10:
        d1, d2, i = (
            d1+(int(cpf[i])(11-i-1))) % 11 if i < 9 else d1, (d2+(int(cpf[i])(11-i))) % 11, i+1
    return (int(cpf[9]) == (11-d1 if d1 > 1 else 0)) and (int(cpf[10]) == (11-d2 if d2 > 1 else 0))


def cpfInvalidos(fonte):
    cpf_invalidos = list()
    cpf_fonte = fatec_operacao[(fatec_operacao["id_fnt"] == fonte)]
    listCpfs = list(cpf_fonte["doc_cli"])
    for cpf in listCpfs:
        if not validaCpf(cpf):
            cpf_invalidos.append(cpf)

    porcentagem = (len(cpf_invalidos) / len(listCpfs)) * 100
    return porcentagem, cpf_invalidos
