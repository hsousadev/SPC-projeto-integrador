# Entrega 1
### Ideia inicial
<p>Para esta entrega, tivemos como ideia inicial a construção de uma aolicação Web que, recebe os lotes de dados, os analisa e faz as alterações necessárias e por fim exibe ao usuário os indicadores correspondentes. Além disso, nosso código irá manipular e analisar os dados diretamente de um banco de dados em SQL, integrado a aplicação construída.</p>
<p>Observando os dados que foram enviados para nosso time, podemos tirar algumas conclusões prévias e também algumas ideia para o andamento do projeto para as próximas fases. Entre essas conclusões, podemos notar que os dados foram extraídos de um banco de dados utilizando uma Query em SQL, que estava disponível no documento. Com relação á aplicação, optamos de início por faze-la em uma interface Web devido à ampla utiilzação no mercado e ao fácil acesso dos dados pelos membros da organização. </p>

### Desenvolvendo a ideia
<p>Nosso grupo desenvolveu funções em Python para extrair alguns indicadores de requisitos dos indicadore que foram solicitados pelo cliente. A partir disso, os dados foram convertidos em SQL para facilitar a manipulação dos mesmos. Na IDE PyCharm, o nosso programa se conecta ao banco de dados com as tabelas já convertidas e extrai os parâmetros necessários para a construção dos indicadores.</p>

### Funções desenvolvidas
- Ajuste de dígitos no CNPJ
- Filtro e contagem de CNPJ's duplicados
- Função genérica para retornar os itens duplicados
- Função para retornar uma lista dos campos nulos
- Função de cálculo dos valores nas tabelas movimento e de operação