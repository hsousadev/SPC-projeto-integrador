import pandas as pd

# Dados Principais
         
fonte = pd.read_excel("dados/importados/STG_FNT_ITT.xlsx")
modalidade = pd.read_excel("dados/importados/STG_MDL.xlsx")
#pagamento = pd.read_excel("dados/principais/STG_PGT.xlsx")
#movimento = pd.read_excel("dados/principais/STG_MVT_CRD.xlsx")

# Dados Complementares
fatec_operacao = pd.read_excel("dados/importados/fatec_opr.xlsx")
fatec_movimento = pd.read_excel("dados/importados/fatec_mvt.xlsx")
fatec_pagamento = pd.read_excel("dados/importados/fatec_pgt.xlsx")



# indice das fontes
indice_fontes = set(list(int(float(str(i).strip()))
                            for i in list(fatec_operacao['id_fnt'])))

def limpa_espacos(df):  # Removendo espaços dos campos das tabelas
    for coluna in df:
        coluna_temporaria = list()
        for campo in df[coluna]:
            if type(campo) == str:
                coluna_temporaria.append(campo.strip())
            else:
                coluna_temporaria.append(campo)
        df[coluna].update(pd.Series(coluna_temporaria))


# lista de dataframes
dataframes = [fatec_operacao, fatec_movimento, fatec_pagamento, modalidade, fonte]

for df in dataframes:  # limpando todas as listas
    limpa_espacos(df)

                
                
def adiciona_coluna_fonte(dataframe): # Nome do dataframe que voce deseja adicionar a coluna fonte
    lista_fontes = list() # lista de fontes a serem adicionadas no dataframe

    for index in list(dataframe['id_opr_cad_pos']):
        if index in list(fatec_operacao['id_opr_cad_pos']):
            for ID in zip(list(fatec_operacao['id_opr_cad_pos']), list(fatec_operacao['id_fnt'])):
                if index == ID[0]:
                    lista_fontes.append(ID[1])
        else:
            lista_fontes.append("Não encontrado")

    return dataframe.insert(loc = dataframe.shape[1], column = "id_fnt", value = lista_fontes)

def adiciona_coluna_modalidade(dataframe):
    lista_modalidades = list()

    for index in list(dataframe['id_opr_cad_pos']):
        if index in list(fatec_operacao['id_opr_cad_pos']):
            for ID in zip(list(fatec_operacao['id_opr_cad_pos']), list(fatec_operacao['cod_mdl'])):
                if index == ID[0]:
                    lista_modalidades.append(ID[1])
        else:
            lista_modalidades.append("Não encontrado")
    
    return dataframe.insert(loc = dataframe.shape[1], column = "cod_mdl", value = lista_modalidades)


def coluna_fonte():
    dataframes = [fatec_movimento, fatec_pagamento]
    for dataframe in dataframes:
        adiciona_coluna_fonte(dataframe)
    return

coluna_fonte()
adiciona_coluna_modalidade(fatec_movimento)

