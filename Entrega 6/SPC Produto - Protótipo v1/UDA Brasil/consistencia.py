import pandas as pd
from data import fatec_operacao, fatec_movimento, fatec_pagamento, modalidade, indice_fontes

lista_modalidade = list(modalidade["COD_MDL"])

def verifica_opr(fonte):
    campos_inconsistentes = fatec_operacao.query(
        f"cod_mdl not in {lista_modalidade}")['cod_mdl'].count()
    return ((campos_inconsistentes / fatec_operacao.shape[0]) * 100)


def consistencia_modalidade_operacao():
    matriz_consistencia = list()
    for fonte in indice_fontes:
        porcentagem = verifica_opr(fonte)
        matriz_consistencia.append([fonte, porcentagem])
    matriz_consistencia.sort()
    return matriz_consistencia

# TABELA MOVIMENTO

def verifica_id(fonte):
    idsInvalidos = list()
    dataframe = fatec_movimento[(fatec_movimento['id_fnt'] == fonte)]
    for index in list(dataframe['id_opr_cad_pos']):
        if index not in list(fatec_operacao['id_opr_cad_pos']):
            idsInvalidos.append(index)
    porcentagem = (len(idsInvalidos) / len(list(dataframe['id_opr_cad_pos']))) * 100
    return porcentagem, idsInvalidos


def consistencia_id_operacao():
    matriz_consistencia = list()
    for fonte in indice_fontes:
        porcentagem = verifica_id(fonte)
        matriz_consistencia.append(fonte, porcentagem[0])
    matriz_consistencia.sort()
    return matriz_consistencia


def verifica_tip_mdl(fonte):
    tipMDL_invalidos = fatec_movimento.query(f"id_fnt == {fonte} and tip_mdl != 'ANT' or tip_mdl != 'ATU' or tip_mdl != 'FUT'")

    ## Usar o .query().sum() para cada condição e ir somando em uma unica variável e assim no final realizar o calculo da porcentagem.
    return 

def consistencia_tipo_modalidade():
    matriz_consistencia = list()
    for fonte in indice_fontes:
        porcentagem = verifica_tip_mdl(fonte)
        matriz_consistencia.append(fonte, porcentagem[0])
    matriz_consistencia.sort()
    return matriz_consistencia