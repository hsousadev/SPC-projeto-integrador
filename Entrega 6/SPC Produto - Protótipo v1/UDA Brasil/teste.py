import pandas as pd
from data import fatec_operacao, fatec_movimento, fatec_pagamento, modalidade, indice_fontes


def consistencia_id(fonte):
    id_invalidos = list()
    dataframe = fatec_operacao[(fatec_operacao["id_fnt"] == fonte)]
    print(dataframe)
    lista_id = list(dataframe['id_opr_cad_pos'])
    for index in lista_id:
        if index not in list(dataframe['id_opr_cad_pos']):
            id_invalidos.append(index)
    return (len(id_invalidos) / dataframe.shape[0]) * 100


def consistencia_id_operacao():
    matriz_consistencia = list()
    for fonte in indice_fontes:
        porcentagem = consistencia_id(fonte)
        matriz_consistencia.append(fonte, porcentagem)
    matriz_consistencia.sort()
    return matriz_consistencia

