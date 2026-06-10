import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dados_tempo = pd.read_excel('/Users/lucasarruda/Study/POS/IA and Data/files_aula/Data Wrangling Python/(1.2) dataset_principal.xls')
dados_merge = pd.read_excel('/Users/lucasarruda/Study/POS/IA and Data/files_aula/Data Wrangling Python/(1.3) dataset_join.xls')

dados_tempo = dados_tempo.rename(columns={'Estudante':'estudante',
                                          'Tempo para chegar à escola (minutos)':'tempo',
                                          'Distância percorrida até a escola (quilômetros)': 'distancia',
                                          'Quantidade de semáforos': 'semaforos',
                                          'Período do dia': 'periodo',
                                          'Perfil ao volante': 'perfil'})


dados_tempo.iloc[3,]
dados_tempo.iloc[:,4] ## indicam vazio na linha
dados_tempo.iloc[2:5,] # note que exclui a posicao final
dados_tempo.iloc[:,3:5] # note que exclui a posicao final
dados_tempo.iloc[2:4,3:5] # note que exclui as posicoes finais
dados_tempo.iloc[5,4]


## detalhar uma variavel em especifico pelo nome

dados_tempo['tempo']
var_tempo = dados_tempo['tempo']

# forma mais simples de acessar, mas por exemplo se a variavel tiver um espaco no nome.
dados_tempo.perfil
var_perfil = dados_tempo.perfil

## se for mais de uma variavel em lista

dados_tempo[['tempo', 'perfil']]
var_tempo_perfil = dados_tempo[['tempo', 'perfil']]

## acessar por atributos semelhantes

select_1 = dados_tempo.loc[:, dados_tempo.columns.str.startswith('per')]

## selecionando variavel por um final em comum 

select_2 = dados_tempo.loc[:, dados_tempo.columns.str.endswith('o')]


## 1. Vamos adicionar uma variavel a um dataset existente, aqui as observacoes do dataset e variavel devem estar igualmente ordenadas

idade = pd.Series([25,28,30,19,20,36,33,48,19,21])

dados_tempo['idade'] = idade


## 2 adicionando linhas ao banco de dados

nova_obs = pd.DataFrame({'periodo':['Tarde'], 'Estudante': ['Roberto'], 'tempo': [40]

})

### adicionar apenas a nova linha

dados_concat = pd.concat([dados_tempo, nova_obs]).reset_index(drop=True) # aqui voce organiza e reseta o index, caso queira manter o index original

## Criar variaveis no nosso bando de dados em base a outras variaveis

dados_tempo['sem_km'] = round((dados_tempo['semaforos'] / dados_tempo['distancia']),2) #como uma formula excel criando uma coluna e ja criando seu dado


## vamos usar 'assign '

labels = {
    'calmo': 'perfil_A',
    'moderado': 'perfil_B',
    'agressivo' : 'perfil_C'
}

df_labels = dados_tempo.assign(novo_perfil = dados_tempo.perfil.map(labels)) # assinei que agora a coluna "novo perfil" vai ser criado essa condicao.
df_labels.info()


## assing para numeros (nao fazer ponderacao arbitraria: Pegar uma variavel categorica com textos)

numeros =  {'calmo': 1,
    'moderado': 2,
    'agressivo' : 3
}

df_numeros = dados_tempo.assign(novo_perfil = dados_tempo.perfil.map(numeros))

# trocando numeros por textos

num_to_text = {
    0: 'zero',
    1: 'um',
    2: 'dois',
    3: 'tres'
} 

df_texto = dados_tempo.assign(novos_semafotos = dados_tempo.semaforos.map(num_to_text))


## Ponderacao arbitraria uma variavel categorica para uma variavel metrica

# Categorizacao

# dados_tempo['faixa'] = np.where(dados_tempo['tempo'] <= 20, 'rapido', np.where((dados_tempo['tempo'] > 20) & (dados_tempo['tempo'] <= 40), np.where(dados_tempo['tempo'] > 40, 'demorado', 'demais')))

dados_tempo['quartis'] = pd.qcut(dados_tempo['tempo'], q=4, labels=['25%','50%','75%','100%']) # fazendo quartis e escolhendo o rotulo de cada uma das 4 partes

df_numeros['novo_perfil'] = df_numeros['novo_perfil'].astype('category')
df_numeros.info()


## Limpeza no df

df_numeros.drop(columns=['periodo', 'perfil'], inplace=True)


#organizando ordem crescente 

df_org_1 = dados_tempo.sort_values(by=['tempo'], ascending=True).reset_index(drop=True)

#organizando em ordem descrescente

df_org_2 = dados_tempo.sort_values(by=['tempo'], ascending=False).reset_index(drop=True)

# organizando por ordem de texto

df_org_3 = dados_tempo.sort_values(by=['periodo'], ascending=True).reset_index(drop=True)
df_org_4 = dados_tempo.sort_values(by=['periodo'], ascending=False).reset_index(drop=True)

# Organizando por mais de um criterio 

df_org_5 = dados_tempo.sort_values(by=['perfil', 'distancia'], ascending=[True, True]).reset_index(drop=True)

## 1. estatisticas descritivas # 09_06_2026


dados_tempo.describe()

# estatistica individuais univariaveis

dados_tempo['tempo'].count() # contagem
dados_tempo['tempo'].mean() # media
dados_tempo['tempo'].median() #mediana
dados_tempo['tempo'].min() #minima
dados_tempo['tempo'].max() #maximo
dados_tempo['tempo'].std() # desvio padrao
dados_tempo['tempo'].var() # variancia
dados_tempo['tempo'].quantile([0.25,0.75]) #quartis
dados_tempo['tempo'].sum() #soma

# Matriz de correlacao de pearson univariaveis entre pares metricas:
dados_tempo[['tempo', 'distancia', 'semaforos']].corr()


# tabela de frequencias para variaveis qualitativas

dados_tempo['periodo'].value_counts() # frequencia absoluta
dados_tempo['perfil'].value_counts(normalize=True) # frequencia relativa

# tabela de frequencias cruzadas para pares de variaveis qualitativas

pd.crosstab(dados_tempo['periodo'], dados_tempo['perfil'])
pd.crosstab(dados_tempo['periodo'], dados_tempo['perfil'], normalize=True)

## 2. Obtendo informações de valores únicos das variáveis

dados_tempo['tempo'].unique()
dados_tempo['periodo'].unique()
dados_tempo['perfil'].nunique() # quantidade de valores únicos

## 3. Criando um banco de dados agrupado (um critério)

dados_periodo = dados_tempo.groupby(['periodo'])

# Gerando estatísticas descritivas

dados_periodo.describe()

# Caso a tabela gerada esteja com visualização ruim no print, pode transpor

dados_periodo.describe().T

# Tamanho de cada grupo

dados_periodo.size()

# Criando um banco de dados agrupado (mais de um critério)

dados_criterios = dados_tempo.groupby(['periodo', 'perfil'])

# Gerando as estatísticas descritivas

dados_criterios.describe().T

# Tamanho de cada grupo

dados_criterios.size()

# Especificando estatísticas de interesse

dados_periodo.agg({'tempo': 'mean',
                   'distancia': 'mean',
                   'periodo': 'count'})


# Filtros de observacoes

filtro_calmo = dados_tempo[dados_tempo['perfil'] == 'calmo']
filtro_quartil = dados_tempo[dados_tempo['quartis'] == '1']

dados_tempo.query('perfil == "calmo"')
dados_tempo.query('quartis == "1"')


#. intersecao criterios
filtro_intersecao = dados_tempo[(dados_tempo['perfil'] == 'calmo') & (dados_tempo['periodo'] == 'Tarde')]

dados_tempo.query('perfil == "calmo" & periodo == "Tarde"' )


filtro_uniao = dados_tempo[(dados_tempo['perfil'] == 'calmo') | (dados_tempo['periodo'] == 'Tarde')]

# utilizando operadores em variaveis metricas
# variavel #tabela[#tabela#coluna#dado]

filtro_tempo_1 = dados_tempo[dados_tempo['tempo'] >= 25]

filtro_tempo_2 = dados_tempo[(dados_tempo['tempo'] > 30) & (dados_tempo['distancia'] <= 25)]

filtro_tempo_3 = dados_tempo[dados_tempo['tempo'].between(25, 40, inclusive='both')]


# comparando com valores de outro objeto utilizando isin()

nomes = pd.Series(["Gabriela", "Gustavo", "Leonor", "Ana", "Julia"])
filtro_contidos = dados_tempo[dados_tempo['estudante'].isin(nomes)]


# dados nao 

filtro_tempo_4 = dados_tempo[~(dados_tempo['tempo'] >= 25)]

# Funcao merge para unir bancos de dados (iniciamos com chaves para declrar as colunas): 

dados_merge.rename(columns={'Estudante': 'estudante'}, inplace=True)

# left
# Observações de dados_tempo -> dados_merge
# Ficam os IDs de dados_tempo

merge_1 = pd.merge(dados_tempo, dados_merge, how='left', on='estudante')

# Right
# Observações de dados_tempo -> dados_merge
# Ficam os IDs de dados_merge

merge_2 = pd.merge(dados_tempo, dados_merge, how='right', on='estudante')

# Outer
# Observações das duas bases de dados constam na base final 
# Ficam todos os IDs presentes nas duas bases

merge_3 = pd.merge(dados_tempo, dados_merge, how='outer', on='estudante')

# Inner
# Somente os IDs que constam nas duas bases ficam na base final 
# É a interseção de IDs entre as duas bases de dados

merge_4 = pd.merge(dados_tempo, dados_merge, how='inner', on='estudante')


# verifcando apenas diferenca entre os bancos

merge_5 = dados_tempo[~ dados_tempo.estudante.isin(dados_merge.estudante)]
merge_6 = dados_tempo[~ dados_tempo.estudante.isin(dados_tempo.estudante)]
#drop duplicates
dados_tempo.drop_duplicates()


# contagem de linhas duplicadas

contagem_dupli = (len(dados_tempo) - len(dados_tempo.drop_duplicates()))

# remocao com algumas variaveis

dados_tempo.drop_duplicates(subset=['estudante', 'perfil'])

# excluindo linhas faltantes com NAs
## contando quantos tem
merge_3.isna().sum()
## Caso queira subistituir NAs por algum elemento
merge_3 = merge_3.assign(quartis = merge_3.quantic.astype('object'))

# repor NA para texto
merge_3.fillna('elemento')

# valor metrico, preenchendo os NAs com a media da coluna.
merge_3['tempo'].fillna(merge_3['tempo'].mean())

# Excluindo observacoes que apresentam valores faltantes
merge_exclui = merge_3.dropna().reset_index(drop=True)

# funcao pandas .melt alterando a estrutura

df_estrutura = pd.melt(dados_tempo,id_vars='estudante',value_vars=['tempo', 'distancia'])