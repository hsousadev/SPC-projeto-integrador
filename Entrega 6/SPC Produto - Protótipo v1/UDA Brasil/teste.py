import pandas as pd
from data import fatec_operacao, fatec_movimento, fatec_pagamento, modalidade, indice_fontes

teste = set(list(fatec_movimento['prd']))
teste2 = set(list(fatec_movimento['tip_mvt']))
