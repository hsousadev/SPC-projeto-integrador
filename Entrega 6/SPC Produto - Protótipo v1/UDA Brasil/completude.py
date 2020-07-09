import pandas as pd
from data import fatec_operacao, fatec_movimento, fatec_pagamento, indice_fontes



fontes_ids = list(int(float(str(i).strip()))
                  for i in list(fatec_operacao['id_fnt']))
fatec_operacao['id_fnt'].update(pd.Series(fontes_ids))


# Função que calcula a quantidade total de campos para um determinada fonte


def campos_totais_opr(fonte):
    return fatec_operacao.query(f"id_fnt == {fonte}")['id_fnt'].count() * fatec_operacao.shape[1]

# Função que calcula quantos campos nulos existem por conta da modalidade D01 e C01, as quais são as únicas que
# precisam da coluna 'sdo_ddr_tfm'


def nulos_permitidos(fonte):
    return fatec_operacao.query(f"sdo_ddr_tfm == 'NULL' and cod_mdl not in ['D01', 'C01'] and id_fnt == {fonte}")['sdo_ddr_tfm'].count()


# Função que retorna a porcentagem de campos nulos de acordo com a fonte, na tabela de operação
def completude_opr(fonte):
    campos_nulos = 0
    # for linha in range(fatec_operacao.shape[1]):
    #     for campo in fatec_operacao.loc[linha]:
    #         if campo['id_fnt'] == fonte:
    #             campos_nulos += fatec_operacao.loc[linha].isna().sum()
    for linha in range(fatec_operacao.shape[0]):
        if fatec_operacao.loc[linha]['id_fnt'] == fonte:
            campos_nulos += fatec_operacao.loc[linha].isna().sum()
            

    nulos_totais = campos_nulos - nulos_permitidos(fonte)
    return 100 - ((nulos_totais / campos_totais_opr(fonte)) * 100)


# Função que integra as 3 funções anteriores, retornando uma lista com a fonte e a porcentagem de sua respectiva
# completude dos dados
def completude_fontes_operacao():
    matriz_completude = list()
    for fonte in indice_fontes:
        porcentagem = completude_opr(fonte)
        matriz_completude.append([fonte, porcentagem])
    matriz_completude.sort()
    return matriz_completude


## TABELA MOVIMENTO
## TESTE - VERIFICANDO SE OS ID'S OPERAÇÃO EXISTEM DENTRO DA TABELA OPERAÇÃO

