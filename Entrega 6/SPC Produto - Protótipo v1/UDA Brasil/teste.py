import pandas as pd
from data import fatec_operacao, fatec_movimento, fatec_pagamento, modalidade, indice_fontes


def verifica_valor(df, coluna, fonte):
    campos_invalidos = list()
    
    for index in zip(df[coluna], df['id_fnt']):
        if index[1] == fonte:
            try:
                float(index[0])
                
            except ValueError:
                if index[0] != 'NULL':
                    campos_invalidos.append(index[0])
    
    porcentagem = 100 - (len(campos_invalidos) / len(df[coluna])) * 100

    return porcentagem, campos_invalidos




def validaNumerico(df, colunas):
    matriz = list([fonte] for fonte in indice_fontes)

    for index in range(len(matriz)):
        campos_inconsistentes = list()

        for coluna in colunas:
            porcentagem = verifica_valor(df, coluna, matriz[index][0])
            campos_inconsistentes.append(porcentagem[0])
    
        porcentagem = sum(campos_inconsistentes) / len(colunas)

        matriz[index].append(porcentagem)
        campos_inconsistentes.clear()
    return matriz

