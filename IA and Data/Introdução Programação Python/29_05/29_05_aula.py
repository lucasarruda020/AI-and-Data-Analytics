import pandas as pd
import numpy as np

notas_pisa = pd.read_csv("/Users/lucasarruda/Study/POS/Introdução Programação Python/(2) notas_pisa.csv", sep=",", decimal=".")

## localizar infos basicas
#print(notas_pisa.info())

## Localizar pelo indice pandas

notas_pisa.iloc[46,2]

## todas as colunas

notas_pisa.iloc[46,]


## Valores de todas variaveis entre

notas_pisa.iloc[0:7,]

## funcao to_numaric tratamento de dados


notas_pisa['mathematics_2022'] = pd.to_numeric(notas_pisa['mathematics_2022'], errors='coerce')
notas_pisa['mathematics_2018'] = pd.to_numeric(notas_pisa['mathematics_2018'], errors='coerce')

notas_pisa['reading_2022'] = pd.to_numeric(notas_pisa['reading_2022'], errors='coerce')
notas_pisa['reading_2018'] = pd.to_numeric(notas_pisa['reading_2018'], errors='coerce')

notas_pisa['science_2022'] = pd.to_numeric(notas_pisa['science_2022'], errors='coerce')
notas_pisa['science_2018'] = pd.to_numeric(notas_pisa['science_2018'], errors='coerce')

pisa_na = notas_pisa.dropna()

# tabela de estatistica descritivas para variaveis quantitativas

notas_pisa[['mathematics_2022', 'reading_2022', 'science_2022']].describe()

#tabela de frequencias variavel
notas_pisa['group'].value_counts()

## filtrar banco de dados num: 
notas_maior = notas_pisa[notas_pisa['mathematics_2022'] > 437]

## filtrar banco de dados string
notas_OECD = notas_pisa[notas_pisa['group'] == 'OECD']

## dois filtros juntos banco[[()] && ([]) ]
notas_pisa[(notas_pisa['group'] == 'OECD') & (notas_pisa['science_2022'] <= 493)]

## Operador logico != 
notas_pisa[(notas_pisa['group'] != 'OECD')]

## tabela ( [tabela['coluna'] operador 'valor' ] )

### nota em leitura no ano de 2022 menor do que 386 ou maior do que 480

criterio = notas_pisa[(notas_pisa['reading_2022'] < 386) | (notas_pisa['reading_2022'] > 480)]

#agrupando dados pelo groupby

pisa_grupo = notas_pisa.groupby(by=['group'])

pisa_grupo.describe().T # o comando '.T' apenas fez a transposicao da tabela. 

## organizand o dataset com base em criterios e possivel ordernar

sort_pisa = notas_pisa.sort_values(by=['mathematics_2022'], ascending=False) #ascending false ordem decrescente e True crescente

### trocar o nome das variaveis

nomes = ['Pais', 'grupo', 'matematica_2022', "leitura_2022", "matematica_2018", "leitura_2018", "ciencia_2022", "ciencia_2018"]

# notas_pisa.columns = nomes 

notas_pisa = notas_pisa.rename(columns={'group': 'grupo_paises'})

## Data Visualization

# Para visualizacao de dados, vamos utilizar seguintes pacotes: pip install matplotlib, seaborn, ploty

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser'
import plotly.graph_objects as go

comercio = pd.read_excel('/Users/lucasarruda/Study/POS/Introdução Programação Python/(2) comercio_global.xlsx')
