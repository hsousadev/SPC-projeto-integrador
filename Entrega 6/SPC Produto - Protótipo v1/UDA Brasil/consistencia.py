import pandas as pd
from data import fatec_operacao, fatec_movimento, fatec_pagamento, modalidade, indice_fontes

lista_modalidade = list(modalidade["COD_MDL"])

'''
INÍCIO DAS ANÁLISES DA TABELA DE OPERAÇÕES
'''

def consistencia_opr(fonte):
    campos_inconsistentes = fatec_operacao.query(
        f"cod_mdl not in {lista_modalidade}")['cod_mdl'].count()
    return 100 - ((campos_inconsistentes / fatec_operacao.shape[0]) * 100)


def consistencia_modalidade_opr():
    matriz_consistencia = list()
    for fonte in indice_fontes:
        porcentagem = consistencia_opr(fonte)
        matriz_consistencia.append([fonte, porcentagem])
    matriz_consistencia.sort()
    return matriz_consistencia


'''
FIM DAS ANÁLISES NA TABELA DE OPERAÇÕES
'''

'''
INÍCIO DAS ANÁLISES DA TABELA DE MOVIMENTO
'''


def consistencia_id_mvt(fonte):
    idsInvalidos = list()

    
    # dataframe = fatec_movimento[(fatec_movimento['id_fnt'] == fonte)]
    # for index in list(dataframe['id_opr_cad_pos']):
    #     if index not in list(fatec_operacao['id_opr_cad_pos']):
    #         idsInvalidos.append(index)
    # porcentagem = (len(idsInvalidos) / len(list(dataframe['id_opr_cad_pos']))) * 100
    # return porcentagem, idsInvalidos


def consistencia_id_operacao_mvt():
    matriz_consistencia = list()
    for fonte in indice_fontes:
        porcentagem = consistencia_id_mvt(fonte)[0]
        matriz_consistencia.append([fonte, porcentagem])
    matriz_consistencia.sort()
    return matriz_consistencia

'''
FIM DAS ANÁLISES DA TABELA DE MOVIMENTO
'''


