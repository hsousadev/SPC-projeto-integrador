import pandas as pd
from data import fatec_operacao, fatec_movimento, fatec_pagamento, indice_fontes
'''
fontes_ids = list(int(float(str(i).strip())) for i in list(fatec_operacao['id_fnt']))
fatec_operacao['id_fnt'].update(pd.Series(fontes_ids))
'''

'''
INÍCIO DAS ANÁLISES NA TABELA DE OPERAÇÕES
'''
# Função que calcula a quantidade total de campos para um determinada fonte


def campos_totais_opr(fonte):
    return fatec_operacao.query(f"id_fnt == {fonte}")['id_fnt'].count() * fatec_operacao.shape[1]

# Função que calcula quantos campos nulos existem por conta da modalidade D01 e C01, as quais são as únicas que
# precisam da coluna 'sdo_ddr_tfm'


def nulos_permitidos_opr(fonte):
    return fatec_operacao.query(f"sdo_ddr_tfm == 'NULL' and cod_mdl not in ['D01', 'C01'] and id_fnt == {fonte}")['sdo_ddr_tfm'].count()


# Função que retorna a porcentagem de campos nulos de acordo com a fonte, na tabela de operação
def completude_opr(fonte):

    referencia_fontes = list(fatec_operacao['id_fnt'])
    campos_nulos = int()

    for linha in range(len(referencia_fontes)):
        if referencia_fontes[linha] == fonte:
            campos_nulos += fatec_operacao.loc[linha].isna().sum()

    nulos_totais = campos_nulos - nulos_permitidos_opr(fonte)
    return 100 - ((nulos_totais / campos_totais_opr(fonte)) * 100)

# Função que integra as 3 funções anteriores, retornando uma lista com a fonte e a porcentagem de sua respectiva
# completude dos dados


def completude_fontes_opr():
    matriz_completude = list()
    for fonte in indice_fontes:
        porcentagem = completude_opr(fonte)
        matriz_completude.append([fonte, porcentagem])
    matriz_completude.sort()
    return matriz_completude

'''
FIM DAS ANÁLISES NA TABELA DE OPERAÇÕES
'''

###################################################################################################

'''
INÍCIO DAS ANÁLISES NA TABELA DE PAGAMENTOS
'''


def campos_totais_pgt(fonte):
    return fatec_pagamento.query(f"id_fnt == {fonte}")['id_fnt'].count() * fatec_pagamento.shape[1]


def completude_fontes_pgt(fonte):
    campos_nulos = int()
    referencia_fontes = list(fatec_pagamento['id_fnt'])
    for linha in referencia_fontes:
        if linha == fonte:
            campos_nulos += fatec_operacao.loc[linha].isna().sum() #Contabilizando campos nulos
            for campo in fatec_operacao.loc[linha]:
                if campo == 'NULL':                                #Contabilizando strings com valor 'NULL'
                    campos_nulos += 1
    campos_totais = campos_totais_pgt(fonte)
    return 100 - ((campos_nulos / campos_totais) * 100)
        

            
            

'''
FIM DAS ANÁLISES NA TABELA DE OPERAÇÕES
'''

## TABELA MOVIMENTO
## TESTE - VERIFICANDO SE OS ID'S OPERAÇÃO EXISTEM DENTRO DA TABELA OPERAÇÃO

