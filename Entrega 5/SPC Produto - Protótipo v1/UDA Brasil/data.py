import pandas as pd
fatec_operacao = pd.read_excel("dados/alterados/fatec_opr.xlsx")
fatec_modalidade = pd.read_excel("dados/principais/STG_MDL.xlsx")
fatec_fonte = pd.read_excel("dados/principais/STG_FNT_ITT.xlsx")
fatec_pagamento = pd.read_excel("dados/principais/STG_PGT.xlsx")
fatec_movimento = pd.read_excel("dados/principais/STG_MVT_CRD.xlsx")

# indice das fontes
indice_fontes = set(list(int(float(str(i).strip()))
                         for i in list(fatec_operacao['id_fnt'])))


def limpa_espacos(df):  # Removendo espaços dos campos das tabelas
    for coluna in fatec_operacao:
        coluna_temporaria = list()
        for campo in df[coluna]:
            if type(campo) == str:
                coluna_temporaria.append(campo.strip())
            else:
                coluna_temporaria.append(campo)
        df[coluna].update(pd.Series(coluna_temporaria))


# lista de dataframes
dataframes = [fatec_operacao, fatec_modalidade,
              fatec_fonte, fatec_movimento, fatec_pagamento]

for df in dataframes:  # limpando todas as listas
    limpa_espacos(df)
