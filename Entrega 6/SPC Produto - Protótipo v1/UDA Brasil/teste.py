import pandas as pd
from data import fatec_operacao, fatec_movimento, fatec_pagamento, modalidade, indice_fontes

for index in list(fatec_movimento['id_opr_cad_pos']):
  print(index)
              
