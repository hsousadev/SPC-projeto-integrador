from completude import completude_fontes_opr
from consistencia import consistencia_id_operacao_mvt, consistencia_modalidade_opr
from data import indice_fontes

def get_ranking():
    
    '''
    for fonte in range(len(indice_fontes)):
        media = (completude[fonte][1] + consistencia[fonte][1]) / 2 
        ranking.append([f"{media:.2f}", completude[fonte][0], f"{completude[fonte][1]:.2f}", f"{consistencia[fonte][1]:.2f}"])
        ranking.sort(reverse=True)
    '''

    temp_ranking = list()
    for fonte in range(len(indice_fontes)):
        completude = completude_fontes_opr()[fonte][1]
        
        consistencia = [consistencia_id_operacao_mvt()[fonte][1], consistencia_modalidade_opr()[fonte][1]]
        consistencia = sum(consistencia) / len(consistencia)

        confiabilidade = 100 #valor temporário

        pontuacao = (completude + confiabilidade + consistencia) / 3
        
        temp_ranking.append([pontuacao, indice_fontes[fonte], completude, confiabilidade, consistencia, fonte + 1]) #'fonte + 1' pois possui o mesmo valor que a posição da fonte

        temp_ranking.sort(reverse = True)

    ranking = list()                   
        
    return ranking
