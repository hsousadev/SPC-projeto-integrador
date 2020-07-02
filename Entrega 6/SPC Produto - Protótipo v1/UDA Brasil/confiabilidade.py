import pandas as pd
from data import fatec_operacao, fonte, indice_fontes

def valida_fonte():
    fontes_sem_indentificação = list()
    for id_fonte in indice_fontes:
        if id_fonte not in list(fonte["id_fonte"]):
            fontes_sem_indentificação.append(id_fonte)
    porcentagem = (len(fontes_sem_indentificação) / fonte.shape[0]) * 100
    return porcentagem, fontes_sem_indentificação



def valida_cpf(cpf):

    # Encontrando o primeiro digito
    cont = 10
    acumulador = 0
    for index in range(len(str(cpf))-2):
        acumulador += int(cpf[index]) * cont
        cont -= 1
    digito = 11 - (acumulador % 11)

    cpf_teste = str(cpf[:9]) + str(digito)

    # Encontrando o segundo digito
    cont = 11
    acumulador = 0
    for index in range(len(cpf_teste) - 1):
        acumulador += int(cpf[index]) * cont
        cont -= 1
    digito = 11 - (acumulador % 11)

    resultado_cpf = cpf_teste + str(digito)
    return resultado_cpf == cpf


def verifica_pessoa():
