from data import fatec_pagamento, fatec_movimento, fatec_operacao, modalidade, indice_fontes


'''
CONFIABILIDADE
'''



    
    




'''
CONSISTÊNCIA
'''

def consistencia(df_base, series_base, series_referencia):
    matriz = list([fonte] for fonte in indice_fontes)
    for fonte in indice_fontes:
        campos_inconsistentes = list()
        for campo in range(len(series_base)):
            if df_base['id_fnt'][campo] == fonte and campo not in series_referencia:
                campos_inconsistentes.append(campo)
        
        porcentagem = 100 - (len(campos_inconsistentes) / len(series_base)) * 100
        matriz[indice_fontes.index(fonte)].append(porcentagem)
    
    return matriz

'''
COMPLETUDE
'''


def completude(DataFrame):
    '''
    As matriz abaixo armazenará os campos incompletos de cada fonte, no seguinte formato
    [fonte, quantidade_incompletos]
    [fonte, quantidade_incompletos]...
    '''
    matriz_fontes_incompletos = list([fonte, 0] for fonte in indice_fontes)
    
    for linha in range(DataFrame.shape[0]):
        if DataFrame.iloc[linha].isnull().sum() > 0 or list(DataFrame.iloc[linha]).count('NULL') > 0: #Checando se há algum campo nulo na linha, tanto NaN quanto 'NULL'
            fonte = DataFrame.iloc[linha]['id_fnt']
            posicao = indice_fontes.index(fonte)
            #Somando o segundo valor da array à soma de campos nulos encontrados na linha
            matriz_fontes_incompletos[posicao][1] += DataFrame.iloc[linha].isnull().sum() + list(DataFrame.iloc[linha]).count('NULL')
    
    matriz_completude_porcentagem = list()

    for fonte in range(len(indice_fontes)):
        #A variável abaixo registra quantos campos existem referentes à fonte possuem a fonte em questão. 
        # Estamos multiplicando pela quantidade de colunas - 1 pois uma das colunas apenas identifica a fonte.
        campos_fonte_total = DataFrame.query(f'id_fnt == {indice_fontes[fonte]}')['id_fnt'].count() * (DataFrame.shape[1] - 1)
        campos_incompletos = matriz_fontes_incompletos[fonte][1]
        porcentagem = 100 - ((campos_incompletos / campos_fonte_total) * 100)
        matriz_completude_porcentagem.append([indice_fontes[fonte], porcentagem])
    
    return matriz_completude_porcentagem


'''
GERAÇÃO DA MATRIZ COM TODOS OS INDICADORES ACIMA, PARA A TABELA DE PAGAMENTO
'''

def indicadores_fatec_pagamento():
    matriz_consistencia_opr = consistencia(fatec_pagamento, fatec_pagamento['id_opr_cad_pos'], fatec_operacao['id_opr_cad_pos'])
    matriz_consistencia_mvt = consistencia(fatec_pagamento, fatec_pagamento['id_mvt_cad_pos'], fatec_movimento['id_mvt_cad_pos'])
    matriz_consistencia_mdl = consistencia(fatec_pagamento, fatec_pagamento['cod_mdl'], modalidade['COD_MDL'])

    matriz_consistencia_final = list()
    for fonte in range(len(indice_fontes)):
        media = (matriz_consistencia_opr[fonte][1] + matriz_consistencia_mvt[fonte][1] + matriz_consistencia_mdl[fonte][1]) / 3
        matriz_consistencia_final.append([indice_fontes[fonte], media])

    
    



    

