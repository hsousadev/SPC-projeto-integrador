#!/usr/bin/env python
# coding: utf-8

# # INDICADOR: INTEGRIDADE

# ## 00. Declarando Bibliotecas

# In[25]:


import pandas as pd 


# ## 1. Criação de dataframes e adaptação

# #### 1.1 Criando os dataframes das bases de dados em Excel

# In[26]:


modalidade = pd.read_excel('dados/STG_MDL.xls')
pagamento = pd.read_excel('dados/STG_PGT.xls')
movimento = pd.read_excel('dados/STG_MVT_CRD.xls')
operacao = pd.read_excel('dados/STG_OPR_ITT.xls')
fonte = pd.read_excel('dados/STG_FNT_ITT.xls')


# #### 1.2 Aplicando padrão de nome de colunas estabelecido pela equipe, apenas para etapa de manipulação

# In[27]:


modalidade.columns = ['id_mod', 'codigo_mod', 'descri_mod', 'DAT_INC_DBO']
pagamento.columns = ['id_pagamento', 'vlr_pago', 'data_vencimento', 'codigo_mod', 'qtd_clientes', 'qtd_pagamento', 'id_fonte', 'tipo_pessoa', 'DAT_RSS_FNT_ITT', 'DAT_INC_DBO']
movimento.columns = ['id_movi', 'vlr_saldo', 'vlr_total_fat', 'vlr_min_fat', 'vlr_parcela_fat', 'qtd_clientes', 'qtd_movi', 'tipo_pessoa', 'id_fonte', 'codigo_mod', 'DAT_RSS_FNT_ITT', 'DAT_INC_DBO']
operacao.columns = ['id_operacao', 'vlr_contrato', 'qtd_parcelas', 'vlr_devido', 'qtd_clientes', 'qtd_operacao', 'id_fonte', 'id_mod', 'tipo_pessoa', 'DAT_RSS_FNT_ITT', 'DAT_INC_DBO']
fonte.columns = ['id_fonte', 'cnpj', 'complemento', 'NOM_COM', 'NOM_RAZ_SCL', 'DAT_INC_DBO']


# #### 1.3 Criando o atributo .nome para facilitar a exibição das tabelas nas respectivas funções

# In[28]:


fonte.nome = 'Fonte'
movimento.nome = 'Movimentações'
operacao.nome = 'Operações'
pagamento.nome = 'Pagamento'
modalidade.nome = 'Modalidade'


# ## 2. Apresentação da situação atual dos dados

# In[29]:


fonte.head(10)


# In[30]:


modalidade.head(10)


# In[31]:


movimento


# In[32]:


operacao.head(15)


# In[33]:


pagamento.head(10)


# ## 3. Funções para análise da Integridade dos dados

# #### 3.1 Ocultar todos os campos nulos sem afetar a integridade. (Condições especificas para as tabelas movimento e operação). 
# Ponderando que, na análise abaixo, dividimos a função em dois dataframes para facilitar a análise, sendo um dataframe somente COM a modalidade C01 e outro dataframe SEM a modalidade C01. Separamos o dataframe em duas partes pois para análisar a modalidade C01, precisamos de condições especificas, como a necessidade das colunas "vlr_contrato" e "vlr_devido". Os valores nulos nas colunas "vlr_contrato" e "vlr_devido" só existem quando não há o atributo da modalidade "C01". Os valores nulos que existem não prejudicam a integridade das informações, mas para melhor apresentação em análise foram ocultados. 

# ##### 3.1.1 Sem a modalidade "CO1" - Tabela 'Operação'

# In[34]:


# Definindo a caracteristica especifica (Dataframe SEM o C01) do dataframe
id_sem_C01 = operacao[(operacao['id_mod'] != 'C01')]

# Criando o dataframe com as caracteristicas especificas e utilizando as colunas necessárias para a análise
df_sem_C01 = pd.DataFrame(id_sem_C01, columns = ['id_operacao', 'qtd_parcelas', 'qtd_clientes', 'qtd_operacao', 'id_fonte', 'id_mod', 'tipo_pessoa', 'DAT_RSS_FNT_ITT', 'DAT_INC_DBO'])


# In[35]:


df_sem_C01


# In[36]:


df_sem_C01.isnull().sum() #conta quantos dados nulos (NÃO HÁ DADOS NULOS QUANDO "OCULTAMOS" as colunas 'vlr_contrato' e 'vlr_devido')


# In[37]:


pd.DataFrame(df_sem_C01['id_mod'].value_counts()) #trazendo ID e suas modalidades


# ##### 3.1.2 Com a modalidade "C01" - Tabela 'Operação'

# In[38]:


# Definindo as caracteristicas especificas (Dataframe COM o C01) do dataframe
id_mod_C01 = operacao[(operacao['id_mod'] == 'C01')]

# Criando o dataframe com as caracteristicas especificas e com todas as colunas
df_com_C01 = pd.DataFrame(id_mod_C01)


# In[39]:


df_com_C01


# In[40]:


df_com_C01.isnull().sum() #conta quantos dados nulos (NÃO HÁ DADOS NULOS QUANDO EXISTE SOMENTE A MODALIDADE C01)


# ##### 3.2 Verifica na Tabela fonte se o Nome Comercial e Razão Social são Strings
# 

# In[41]:


def checar_string(Fonte):
    NOM = pd.DataFrame(Fonte, columns = ['NOM_COM', 'NOM_RAZ_SCL'])
    NOM_COM = []
    RAZ_SCL = []
    cont_a = 0
    cont_b = 0
    for x in NOM.columns:
        for y in NOM[x]:
            
            if x == 'NOM_COM':
                cont_a += 1
                if type(y) != str:
                    NOM_COM.append(cont_a)
                    
            if x == 'NOM_RAZ_SCL':
                cont_b += 1
                if type(y) != str:
                    RAZ_SCL.append(cont_b)
                    
    print(f'''
    Foram identificados {len(NOM_COM)} dados incoerentes na coluna Nome Comercial
    e na coluna Nome Razão Social foram identificados {len(RAZ_SCL)} dados incoerentes''')
    
            
FONTE = checar_string(fonte)
FONTE


# #### 3.2 Validação de CNPJs
# Nessa função o objetivo é você validar todos os CNPJ's, verificando os numeros de digitos

# In[42]:


valida_cnpj = pd.DataFrame(fonte, columns = ['cnpj', 'complemento'])


# In[43]:


# Declarando listas e variaveis
cnpj = []
complemento = []
certos_cnpj = []
certos_complemento = []

# Verificando se a primeira parte do CPJN possui 10 digitos
for x in valida_cnpj['cnpj']:
    if len(str(x)) == 10:
        cnpj.append(str(x))
    else:
        cnpj.append('a')

# Verificando se a segunda parte do CNPJ possui 4 digitos
for x in valida_cnpj['complemento']:
    if len(str(x)) == 4:
        complemento.append(str(x))
    else:
        complemento.append('a')

# Verificando se ao somar as duas partes do CNPJ irá dar 14 digitos
for x in range(valida_cnpj.shape[0]):
    if len(cnpj[x]) + len(complemento[x]) == 14:
        certos_cnpj.append(cnpj[x])
        certos_complemento.append(complemento[x])
        
validos = fonte['cnpj'].isin(certos_cnpj)
cnpj_validos = fonte[validos]
cnpj_validos


# In[44]:


fonte[validos].shape[0]


# #### 3.3 Validação IDs
# Nesta função, temos o objetivo de identificar se os ID's possuem continuidade, e indentificar os ID's que estão faltando.
# 
# Exemplo:
# (1,2,3,5,7,8,9)
# 
# Estão faltando os ID's 4 e 6.

# In[45]:


def gap_id(df):
    IDs = df[df.columns[0]].to_list()
    padrao = range(min(IDs), max(IDs) + 1)
    faltante = list()
    for ID in padrao:
        if ID not in IDs:
            faltante.append(ID)
    if len(faltante) == 0:
        print(f"100% dos ID's da tabela {df.nome} são sequenciais, pois não apresentam nenhum gap.")
        return
    print(f"Existe um gap de {(len(faltante)/len(list(IDs))) * 100:.3f}% na sequência de ID's da tabela {df.nome}")


# In[51]:


analisa_id_fonte = gap_id(fonte)
analisa_id_operacao = gap_id(operacao)
analisa_id_modalidade = gap_id(modalidade)
analisa_id_pagamento = gap_id(pagamento)
analisa_id_movimentacao = gap_id(movimento)


# In[52]:


gap_id(fonte)


# #### 3.4 Validação das modalidades nas tabelas

# In[ ]:


def valida_modalidade(dataframe):
    invalidos = list()
    referencia = [ID for ID in modalidade['cod_modalidade']]
    amostra = [ID for ID in dataframe['id_mod']]
    for ID in amostra:
      if ID not in referencia:
        invalidos.append(ID)

    if len(invalidos) == 0:
      print(f"100% dos ID's da tabela {dataframe.nome} estão referenciados na tabela de fontes")

    else:
      porcentagem = (len(invalidos) / len(amostra)) * 100
      print(f"{porcentagem}% dos ID's da tabela de {dataframe.nome} não estão referenciados na tabela de fontes. Os ID's incorretos estão listados abaixo:")
      print(invalidos)


# #### 3.5 Formatando data de vencimento

# In[48]:


'Formata a data de vencimento'
def Formata_DATAVENCIMENTO(DataFrame):
    DataCerta = []
    DataFrame = DataFrame['data_vencimento'].to_list()
    for i in DataFrame:
        if len(str(i)) == 8:
            dia = str(i)[0:2]
            mes = str(i)[2:4]
            ano = str(i)[4:]
            if int(dia) < 32 and int(mes) < 13:
                dat = str(i)[0:2] + '-' + str(i)[2:4] + '-' + str(i)[4:]
            else:
                dat = 'Data possui informações invalidas'  
            DataCerta.append(dat)
    return DataCerta



Formata_DATAVENCIMENTO(pagamento)


# In[54]:





# In[ ]:




