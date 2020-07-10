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
