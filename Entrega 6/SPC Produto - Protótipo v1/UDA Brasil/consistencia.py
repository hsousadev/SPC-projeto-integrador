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


# LOGICA PRECISA SER ATUALIZADA, NÃO ESTA DE ACORDO COM AS REGRAS DE NEGOCIO. (LISTA DE ID's) O numero de ID'S INVALIDOS VAI SER MAIOR QUE O REAL.
def consistencia_id(fonte):
    id_invalidos = list()
    dataframe = fatec_operacao[(fatec_operacao["id_fnt"] == fonte)]
    lista_id = zip(list(dataframe['id_opr_cad_pos']), list(dataframe['id_fnt']))
    for index in list(fatec_movimento['id_opr_cad_pos']):
        if index not in lista_id:
            id_invalidos.append(index)
    return (len(id_invalidos) / dataframe.shape[0]) * 100

# criar um zip das listas id_opr e id_fnt da tabela operação. Comparar com a lista id_opr da tabela movimento e identificar a fonte.

def consistencia_id_operacao():
    matriz_consistencia = list()
    for fonte in indice_fontes:
        porcentagem = consistencia_id(fonte)
        matriz_consistencia.append(fonte, porcentagem)
    matriz_consistencia.sort()
    return matriz_consistencia
