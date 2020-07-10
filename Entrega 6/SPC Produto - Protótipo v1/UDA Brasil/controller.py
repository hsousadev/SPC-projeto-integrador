#from completude import completude_fontes_opr
#from consistencia import consistencia_id_operacao_mvt, consistencia_modalidade_opr
from data import indice_fontes
from operacao import indicadores_fatec_operacao

operacao = indicadores_fatec_operacao()

# consistencia_id_operacao_mvt = consistencia_id_operacao_mvt()
# consistencia_modalidade_opr = consistencia_modalidade_opr()
# completude_fontes_opr = completude_fontes_opr()
'''
GET_RANKING ANTIGO
def get_ranking():

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
'''

def get_ranking():
    ranking = list()
    
    for fonte in range(len(indice_fontes)):
        consistencia = operacao[fonte][1]
        completude = operacao[fonte][2]
        confiabilidade = operacao[fonte][3]
        pontuacao = (consistencia + completude + confiabilidade) / 3
        #A pontuação é adicionada primeiro para que o método sort possa ordenar a lista de acordo com a pontuação
        
        ranking.append([pontuacao, indice_fontes[fonte], completude, consistencia, confiabilidade])        
    
        #Aqui é realizada a ordenação, de forma reversa para a maior pontuação vir primeiro
    
    ranking.sort(reverse=True)

    #Este for adiciona a colocação das fontes no ranking, na última posição de cada lista
    for posicao in range(len(ranking)):
        ranking[posicao].append(posicao + 1)
    print('Retornando ranking')
    return ranking