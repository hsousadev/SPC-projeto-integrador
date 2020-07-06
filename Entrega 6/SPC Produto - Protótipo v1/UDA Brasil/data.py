import pandas as pd

# Dados Principais
fonte = pd.read_excel("dados/principais/STG_FNT_ITT.xlsx")
modalidade = pd.read_excel("dados/principais/STG_MDL.xlsx")
pagamento = pd.read_excel("dados/principais/STG_PGT.xlsx")
movimento = pd.read_excel("dados/principais/STG_MVT_CRD.xlsx")

# Dados Complementares
fatec_operacao = pd.read_excel("dados/alterados/fatec_opr.xlsx")
fatec_movimento = pd.read_excel("dados/alterados/fatec_mvt.xlsx")
fatec_pagamento = pd.read_excel("dados/alterados/fatec_pgt.xlsx")


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
dataframes = [fatec_operacao, modalidade,
              fonte, movimento, pagamento]

for df in dataframes:  # limpando todas as listas
    limpa_espacos(df)
