import pandas as pd
from data import fatec_operacao, fatec_fonte, indice_fontes, modalidade

# Declarando variáveis globais

referencia_fonte = list(fatec_operacao['id_fnt'])


# Este arquivo irá análisar cada fonte e irá retornar os indicadores já calculados

'''
Funções que retornam listas de id's invalidos (usar para a criação do relatório):

- documentosInvalidos
'''


'''
Indicadores de confiabilidade da tabela fatec operacao
'''

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
    return novo == inteiros


def documentosInvalidos(indice_fontes):
    matriz = list([fonte] for fonte in indice_fontes)
    cpf_invalidos = list()
    cnpj_invalidos = list()
    #dataframe = fatec_operacao[(fatec_operacao["id_fnt"] == fonte)]
    listDoc = [list(fatec_operacao["doc_cli"]), list(fatec_operacao["tip_cli"]), referencia_fonte]

    
    # for index in range(len(listDoc)):
    #     if listDoc[1][index] == "F":
    #         if not validaCpf(listDoc[0][index]):
    #             cpf_invalidos.append(listDoc[0][index])
    #             matriz.append()
        
    #     else:
    #         if not validaCnpj(listDoc[0][index]):
    #              cnpj_invalidos.append(listDoc[0][index])


    # for fonte in referencia_fonte:

    

    porcentagem = ((len(cpf_invalidos) + len(cnpj_invalidos)) / len(listDoc)) * 100
    return porcentagem, cpf_invalidos, cnpj_invalidos


def datasInvalidas_operacao(fonte):
    datas_invalidas = list()
    dataframe = fatec_operacao[(fatec_operacao['id_fnt'] == fonte)]
    for index in zip(list(dataframe['id_opr_cad_pos']), list(dataframe['dat_vct_ult_pcl'])):
        if len(index[1]) < 8:
            datas_invalidas.append(index)
    porcentagem = (len(datas_invalidas) / dataframe.shape[0]) * 100
    return porcentagem, datas_invalidas


'''
Indicadores de consistencia da tabela fatec operacao
'''

def consistencia_opr(fonte):
    lista_modalidade = list(modalidade['COD_MDL'])
    campos_inconsistentes = fatec_operacao.query(f"cod_mdl not in {lista_modalidade}")['cod_mdl'].count()
    return 100 - ((campos_inconsistentes / fatec_operacao.shape[0]) * 100)



'''
Abaixo estamos contatenando todas as funções no seu respectivo indicador
'''

# Irá conter todos os indicadores de confiabilidade da tabela fatec operacao
# Serve para tirar a média de todos os indicadores de confiabilidade
def indicador_confiabilidade(fonte):
    documentos_invalidados = documentosInvalidos(fonte)
    datas_invalidas = datasInvalidas_operacao(fonte)


    valor = list(documentos_invalidados[0], datas_invalidas[0])
    porcentagem = sum(valor) / len(valor)
    return porcentagem

# irá conter todos os indicadores de consistencia da tabela fatec operacao
def indicador_consistencia(fonte): 
    return


# Retorna a matriz de confiabilidade, completude e consistencia da fonte
def indicadores_fatec_operacao(fonte): 
    matriz_fatec_operacao = list()
    matriz_fatec_operacao.append(fonte)
    matriz_fatec_operacao.append(indicador_confiabilidade(fonte))
    matriz_fatec_operacao.append(indicador_consistencia(fonte))

    return