import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dados_tempo = pd.read_excel('/Users/lucasarruda/Study/POS/IA and Data/files_aula/Data Wrangling Python/(1.2) dataset_principal.xls')
dados_merge = pd.read_excel('/Users/lucasarruda/Study/POS/IA and Data/files_aula/Data Wrangling Python/(1.3) dataset_join.xls')


## Ajustar o nome das variaveis

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
