import pandas as pd
from data import fatec_operacao, fatec_movimento, fatec_pagamento, modalidade, indice_fontes

def teste():
    teste = list()
    for ID in list(fatec_movimento['id_opr_cad_pos']):
        if ID in list(fatec_operacao['id_opr_cad_pos']):
            teste.append(ID)
    return len(teste)
