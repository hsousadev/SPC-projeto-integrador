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

## TABELA MOVIMENTO

def consistencia_id(fonte): # LOGICA PRECISA SER ATUALIZADA, NÃO ESTA DE ACORDO COM AS REGRAS DE NEGOCIO. (LISTA DE ID's) O numero de ID'S INVALIDOS VAI SER MAIOR QUE O REAL.  
    id_invalidos = list()
    dataframe = fatec_operacao[(fatec_operacao["id_fnt"] == fonte)]
    lista_id = list(fatec_movimento['id_opr_cad_pos'])
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





'''
def verifica_data():
    dataframe = fatec_movimento[(fatec_movimento[''])]

def consistencia_dat_vct():
    matriz_consistencia = list()
    for fonte in indice_fontes:
        porcentagem = 
'''