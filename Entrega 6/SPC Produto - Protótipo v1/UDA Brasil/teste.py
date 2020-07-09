import pandas as pd
from data import fatec_operacao, fatec_movimento, fatec_pagamento, modalidade, indice_fontes

def adiciona_coluna_fonte(dataframe):
    lista_fontes = list() # lista de fontes a serem adicionadas no dataframe

    for index in list(dataframe['id_opr_cad_pos']):
        if index in list(fatec_operacao['id_opr_cad_pos']):
            for ID in zip(list(fatec_operacao['id_opr_cad_pos']), list(fatec_operacao['id_fnt'])):
                if index == ID[0]:
                    lista_fontes.append(ID[1])
        else:
            lista_fontes.append("Não encontrado")

    return dataframe.insert(loc = dataframe.shape[1], column = "id_fnt", value = lista_fontes)
