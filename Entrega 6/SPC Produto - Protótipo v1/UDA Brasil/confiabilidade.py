import pandas as pd
from data import fatec_operacao, fatec_movimento, fatec_pagamento, fonte, indice_fontes

class Operacao(object):
    def __init__(self, DataFrame):
        self.df = DataFrame
    def consistenciaColunaIdOpr(self):
        contInconsistentes = 0
        for linha in self.df['id_opr_cad_pos']:
            if type(linha) != str or str(linha)[-4] != '-':
                contInconsistentes += 1
        return contInconsistentes
    

def valida_fonte():
    fontes_sem_indentificação = list()
    for id_fonte in indice_fontes:
        if id_fonte not in list(fonte["id_fonte"]):
            fontes_sem_indentificação.append(id_fonte)
    porcentagem = (len(fontes_sem_indentificação) / fonte.shape[0]) * 100
    return porcentagem, fontes_sem_indentificação


def validaCpf(cpf, d1=0, d2=0, i=0):

    while i<10:
        d1,d2,i=(d1+(int(cpf[i])*(11-i-1)))%11 if i<9 else d1,(d2+(int(cpf[i])*(11-i)))%11,i+1
    return (int(cpf[9])==(11-d1 if d1>1 else 0)) and (int(cpf[10])==(11-d2 if d2>1 else 0))


def validaCnpj(cnpj):
    str(cnpj)

    if (not cnpj) or (len(cnpj) < 14):
        return False

    # Pega apenas os 12 primeiros dígitos do CNPJ e gera os 2 dígitos que faltam
    inteiros = list(map(int, cnpj))
    novo = inteiros[:12]

    mascara_validacao = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2] # Fornecida pela receita federal
    while len(novo) < 14:
        r = sum([x*y for (x, y) in zip(novo, mascara_validacao)]) % 11
        if r > 1:
            f = 11 - r
        else:
            f = 0
        novo.append(f)
        mascara_validacao.insert(0, 6)

    # Se o número gerado coincidir com o número original, é válido
    if novo == inteiros:
        return True
    return False


def documentosInvalidos(fonte):
    cpf_invalidos = list()
    cnpj_invalidos = list()
    dataframe = fatec_operacao[(fatec_operacao["id_fnt"] == fonte)]
    listDoc = [list(dataframe["doc_cli"]), list(dataframe["tip_cli"])]
    
    for index in range(len(listDoc)):
        if listDoc[1][index] == "F":
            if not validaCpf(listDoc[0][index]):
                cpf_invalidos.append(listDoc[0][index])
        
        else:
            if not validaCnpj(listDoc[0][index]):
                cnpj_invalidos.append(listDoc[0][index])
    

    porcentagem = ((len(cpf_invalidos) + len(cnpj_invalidos)) / len(listDoc)) * 100
    return porcentagem, cpf_invalidos, cnpj_invalidos


def valida_documentos():
    matriz_confiabilidade = list()
    for fonte in indice_fontes:
        porcentagem = documentosInvalidos(fonte)
        matriz_confiabilidade.append(fonte, porcentagem[0])
    matriz_confiabilidade.sort()
    return matriz_confiabilidade


def datasInvalidas_operacao(fonte):
    datas_invalidas = list()
    dataframe = fatec_operacao[(fatec_operacao['id_fnt'] == fonte)]
    for index in zip(list(dataframe['id_opr_cad_pos']), list(dataframe['dat_vct_ult_pcl'])):
        if len(index[1]) < 8:
            datas_invalidas.append(index)
    porcentagem = (len(datas_invalidas) / dataframe.shape[0]) * 100
    return porcentagem


def valida_data_operacao():
    matriz_confiabilidade = list()
    for fonte in indice_fontes:
        porcentagem = datasInvalidas_operacao(fonte)
        matriz_confiabilidade.append(fonte, porcentagem[0])
    matriz_confiabilidade.sort()
    return matriz_confiabilidade


def datasInvalidas_movimento(fonte):
    datas_invalidas = list()
    dataframe = fatec_operacao[(fatec_operacao['id_fnt'] == fonte)]
    for index in zip(list(dataframe['id_mvt_cad_pos']), list(dataframe['dat_vct'])):
        if len(index[1]) < 8:
            datas_invalidas.append(index)
    porcentagem = (len(datas_invalidas) / dataframe.shape[0]) * 100
    return porcentagem


def valida_data_movimento():
    matriz_confiabilidade = list()
    for fonte in indice_fontes:
        porcentagem = datasInvalidas_movimento(fonte)
        matriz_confiabilidade.append(fonte, porcentagem[0])
    matriz_confiabilidade.sort()
    return matriz_confiabilidade


def datasInvalidas_pagamento(fonte):
    datas_invalidas = list()
    dataframe = fatec_operacao[(fatec_operacao['id_fnt'] == fonte)]
    for index in zip(list(dataframe['id_pgt_cad_pos']), list(dataframe['dat_pgt'])):
        if len(index[1]) < 8:
            datas_invalidas.append(index)
    porcentagem = (len(datas_invalidas) / dataframe.shape[0]) * 100
    return porcentagem


def valida_data_pagamento():
    matriz_confiabilidade = list()
    for fonte in indice_fontes:
        porcentagem = datasInvalidas_pagamento(fonte)
        matriz_confiabilidade.append(fonte, porcentagem[0])
    matriz_confiabilidade.sort()
    return matriz_confiabilidade


def validaNumerico(df, coluna):
    contInvalidos = int()
    camposInvalidos = list()
    
    for campo in df[coluna]:
        try:
            float(campo)
            
        except ValueError:
            if campo != 'NULL':
                contInvalidos += 1
                camposInvalidos.append(campo)
                
    try:
        porcentagem = (1 - (len(coluna) / contInvalidos)) * 100
    
    except ZeroDivisionError:
        porcentagem = 100
        
    return porcentagem, camposInvalidos



