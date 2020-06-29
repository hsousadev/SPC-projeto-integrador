import pandas as pd 

fatec_operacao = pd.read_excel("dados/alterados/fatec_opr.xlsx")
modalidade = pd.read_excel("dados/principais/STG_MDL.xlsx")

lista_modalidade = list(modalidade["COD_MDL"])

def consistencia_opr(fonte):
    campos_inconsistentes = fatec_operacao.query(f"cod_mdl not in {lista_modalidade}")['cod_mdl'].count()
    return 100 - ((campos_inconsistentes / fatec_operacao.shape[0]) * 100)


def consistencia_modalidade_operacao():
    indice_fontes = set(list(int(float(str(i).strip())) for i in list(fatec_operacao['id_fnt'])))
    matriz_consistencia = list()
    for fonte in indice_fontes:
        porcentagem = consistencia_opr(fonte)
        matriz_consistencia.append([porcentagem, fonte])
    matriz_consistencia.sort(reverse=True)
    return matriz_consistencia

consistencia_modalidade_operacao()