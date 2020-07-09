import pandas as pd
from data import fatec_operacao, fatec_movimento, fatec_pagamento, modalidade, indice_fontes

lista_modalidade = list(modalidade["COD_MDL"])

def consistencia_opr(fonte):
    campos_inconsistentes = fatec_operacao.query(
        f"cod_mdl not in {lista_modalidade}")['cod_mdl'].count()
    return ((campos_inconsistentes / fatec_operacao.shape[0]) * 100)


def consistencia_modalidade_operacao():
    matriz_consistencia = list()
    for fonte in indice_fontes:
        porcentagem = consistencia_opr(fonte)
        matriz_consistencia.append([fonte, porcentagem])
    matriz_consistencia.sort()
    return matriz_consistencia

# TABELA MOVIMENTO

def consistencia_id(fonte):
    idsInvalidos = list()
    for 




def consistencia_id_operacao():
    matriz_consistencia = list()
    for fonte in indice_fontes:
        porcentagem = consistencia_id(fonte)
        matriz_consistencia.append(fonte, porcentagem)
    matriz_consistencia.sort()
    return matriz_consistencia
