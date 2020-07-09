from completude import completude_fontes_opr
from consistencia import consistencia_id_operacao_mvt, consistencia_modalidade_opr
from data import indice_fontes

consistencia_id_operacao_mvt = consistencia_id_operacao_mvt()
consistencia_modalidade_opr = consistencia_modalidade_opr()
completude_fontes_opr = completude_fontes_opr()

def get_ranking():

    '''
    for fonte in range(len(indice_fontes)):
        media = (completude[fonte][1] + consistencia[fonte][1]) / 2 
        ranking.append([f"{media:.2f}", completude[fonte][0], f"{completude[fonte][1]:.2f}", f"{consistencia[fonte][1]:.2f}"])
        ranking.sort(reverse=True)
    '''

    ranking = list()
    for fonte in range(len(indice_fontes)):
        completude = completude_fontes_opr[fonte][1]
        
        consistencia = (consistencia_id_operacao_mvt[fonte][1] + consistencia_modalidade_opr[fonte][1]) / 2

        confiabilidade = 100 #valor temporário

        pontuacao = (completude + confiabilidade + consistencia) / 3
        
        ranking.append([f'{pontuacao:.2f}', indice_fontes[fonte], f'{completude:.2f}', f'{confiabilidade:.2f}', f'{consistencia:.2f}']) #'fonte + 1' pois possui o mesmo valor que a posição da fonte

        ranking.sort(reverse = True)

    for posicao in range(len(ranking)):
        ranking[posicao].append(posicao + 1)
                    
    return ranking
