import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser'
import plotly.graph_objects as go
import pandas as pd
import numpy as np

comercio = pd.read_excel('/Users/lucasarruda/Study/POS/Introdução Programação Python/(2) comercio_global.xlsx')

# Vamos iniciar por uma variavel qualitativa, o mercado aonde ocorreu a venda, como eh uma variavel categorica, vamos criar um grafico de contagem (countplot)

plt.figure(figsize=(6,4), dpi = 100)
sns.countplot(data=comercio, x="market")
##### SHOW plt.show()


##podemos escolher a ordem de apresentacao reorganizando os niveis da variavel

plt.figure(figsize=(6,4), dpi = 100)
sns.countplot(data=comercio, x="market", order=["APAC", "LATAM", "EU", "Africa", "EU", "EMEA", "Canada"], color= "blue")
plt.title("Analise por mercado", fontsize=20)
plt.xlabel("Mercado",fontsize=15)
plt.ylabel("contagem", fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
##### SHOW plt.show()



###conhecendo paletas

palette = sns.color_palette("bright")
sns.palplot(palette)
##### SHOW plt.show()

palette = sns.color_palette("Paired")
sns.palplot(palette)
##### SHOW plt.show()

#palette = sns.color_palette("Rocket")
#sns.palplot(palette)
##### SHOW plt.show()


# Alterar o tema do grafico e adicionar as contagens

plt.figure(figsize=(6,4), dpi = 100)
ax = sns.countplot(data=comercio, x="market", hue="market", order=["APAC", "LATAM", "EU", "Africa", "EU", "EMEA", "Canada"], palette='viridis', legend=False)
for container in ax.containers: ax.bar_label(container, fontsize=12) #camadas e rotulos das barras "bar_label"
plt.title("Analise por mercado", fontsize=20)
plt.xlabel("Mercado",fontsize=15)
plt.ylabel("contagem", fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
##### SHOW plt.show()

## Nova ordem feita por meia de contatos e organizada em descrescente.
plt.figure(figsize=(10,9), dpi = 100)
ax = sns.countplot(data=comercio, x="market", hue="market", order=comercio['market'].value_counts(ascending=False), palette='viridis', legend=False)
for container in ax.containers: ax.bar_label(container, fontsize=12)
plt.title("Analise por mercado", fontsize=20)
plt.xlabel("Mercado",fontsize=15)
plt.ylabel("contagem", fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
##### SHOW plt.show()


# VAMOS AJSUTAR OS DADOS DE INTERESSE GERANDO UMA MEDIA POR GRUPO

comercio_agrupado = comercio[['category', 'profit']].groupby(by=['category']).mean()
comercio_agrupado = comercio_agrupado.sort_values(by=['profit'], ascending=False).reset_index() ## Funcao que tira o indice e transforma numa coluna/variavel

## gerando o grafico de barras
plt.figure(figsize=(6,4), dpi = 100)
ax1 = sns.countplot(data=comercio, x="market", hue="market", order=comercio['market'].value_counts(ascending=False), palette='viridis', legend=False)
for container in ax.containers: ax1.bar_label(container, fmt='%,2f', padding=3, fontsize=12) #fmt is formatar
plt.title("Analise por mercado", fontsize=20) 
plt.xlabel("Mercado",fontsize=15)
plt.ylabel("contagem", fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
### SHOW plt.show()


# Gerando grafico de barras 
pizza = pd.crosstab(index = comercio['segment'], columns = 'segmento', normalize = True).sort_values('segmento', ascending = False)

## Plotando o gráfico
plt.figure(figsize=(6,4), dpi = 100)
plt.pie(pizza['segmento'], 
        labels = pizza.index, 
        colors = sns.color_palette('pastel'), 
        autopct='%.0f%%', # nº de casas decimais 
        textprops={'fontsize': 20}, # tamanho da fonte
        pctdistance = 0.6) # posição dos percentuais
plt.title('Análise por Segmento',fontsize=20)
### SHOW plt.show()


# Histograma variaveis metricas

plt.figure(figsize=(6,4), dpi = 100)
sns.histplot(data=comercio, x="sales", bins=50) #Funcao do histograma "histplot", ˜bins: eh a quantidade de barra, Sales eh o grafico que sera contado
plt.xlabel('Valor das Vendas',fontsize=15)
plt.ylabel('Frequência',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
#### SHOW plt.show()

## visualizando a distribuicao de vendas
hist_vendas = comercio[comercio['sales'] < 1000]
plt.figure(figsize=(6,4), dpi = 100)
sns.histplot(data=hist_vendas, x="sales", bins=30) #Funcao do histograma "histplot", ˜bins: eh a quantidade de barra, Sales eh o grafico que sera contado
plt.xlabel('Valor das Vendas',fontsize=15)
plt.ylabel('Frequência',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
### Show plt.show()


## Detalhando um pouco mais o grafico
plt.figure(figsize=(6,4), dpi = 100)
sns.histplot(data=hist_vendas, x="sales", bins=range(0,1100,100), color='blue', alpha=0.6, kde=True) # Alpha da transparencia para barras, KDE ajuste suavizado para seu histograma
plt.ylabel('Frequência',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
## SHOW plt.show()


# Scatterplot escolha suas variaveis de eixos x e y


atlas_ambiental = pd.read_excel("/Users/lucasarruda/Study/POS/Introdução Programação Python/(2) atlas_ambiental.xlsx")
plt.figure(figsize=(9,6), dpi=100)
sns.scatterplot(data=atlas_ambiental, x='renda', y='escolaridade')
plt.show()

## Adicionando uma variavel a mais que eh aumentando o tamanho dos icones pela idade
plt.figure(figsize=(9,6), dpi=100)
sns.scatterplot(data=atlas_ambiental, x='renda', y='escolaridade', size='idade')
plt.title("Indicadores dos distritos", fontsize=20)
plt.xlabel('Renda',fontsize=15)
plt.ylabel('Escolaridade',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Vamos criar uma nova variavel se esta acima ou abaixo da media.

print(atlas_ambiental['favel'].mean())

atlas_ambiental.loc[atlas_ambiental["favel"]<5.93, "indica_favel"] = "Abaixo"
atlas_ambiental.loc[atlas_ambiental["favel"]>=5.93, "indica_favel"] = "Acima"
sns.scatterplot(data=atlas_ambiental, x='renda', y='escolaridade', size='idade', hue="indica_favel") ## Hue vai muda a cor dos pontinhos para cada indicador.
plt.title("Indicadores dos distritos", fontsize=20)
plt.xlabel('Renda',fontsize=15)
plt.ylabel('Escolaridade',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()



#Vamos criar uma para mortlidade

print(atlas_ambiental['mortalidade'].mean())
atlas_ambiental.loc[atlas_ambiental["mortalidade"]<5.93, "mort"] = "Abaixo"
atlas_ambiental.loc[atlas_ambiental["mortalidade"]>=5.93, "mort"] = "Acima"

sns.scatterplot(data=atlas_ambiental, x='renda', y='escolaridade', size='idade', hue="indica_favel", style="mort") ## vai muda o icone da metrica de acordo com o booleano
plt.title("Indicadores dos distritos", fontsize=20)
plt.xlabel('Renda',fontsize=15)
plt.ylabel('Escolaridade',fontsize=15)
plt.legend(bbox_to_anchor=(1,1),fontsize=9)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()


# regplot duas variaveis eixo x e y mas faz ajuste linear

plt.figure(figsize=(9,6), dpi=100)
sns.regplot(data=atlas_ambiental, x='renda', y='escolaridade', size='idade')
plt.title("Indicadores dos distritos", fontsize=20)
plt.xlabel('Renda',fontsize=15)
plt.ylabel('Escolaridade',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Grafico de linhas chamado de lineplot
receita = pd.read_excel("Introdução Programação Python/(2) receita_empresas.xlsx")


plt.figure(figsize=(9,6), dpi=100)
sns.lineplot(data=receita, x="ano", y="receita", hue="id_empresa") # hue grafico para cada empresa uma variavel categorica
plt.show()


plt.figure(figsize=(15,9), dpi = 600)
sns.lineplot(data=receita, x="ano", y="receita", hue="id_empresa", marker="o") # argumento marca os angulos
plt.title("Receita de Vendas",fontsize=20)
plt.xlabel('Ano',fontsize=15)
plt.ylabel('Receita Anual de Vendas',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(title='Empresa', loc='upper left', fontsize=12)
plt.show()



# Grafico interativo usando "px" plotly.express 
fig_line = px.line(receita,
                   x='ano',
                   y='receita',
                   color='id_empresa',
                   markers=True,
                   title='Receita de vendas', labels={
                       'ano': 'Ano', 'receit': 'receita anual de vendas', 'id_empresa':'empresas'
                   })
fig_line.show()

### salvando 
fig_line.write_html('grafico_linhas.html')


# Grafico de calor hitmap 

vendas_regional = pd.read_excel("/Users/lucasarruda/Study/POS/Introdução Programação Python/(2) vendas_regiao.xlsx")

vendas_reg = vendas_regional[['produtoA', 'produtoB', 'produtoC']]


### gerar vendas de correlacoes entre variaveis de Pearson
corr = vendas_reg.corr()
## primeiro vc gera um grafico vazio.
fig_heat = go.Figure()

fig_heat.add_trace( 
    go.Heatmap( #add quais tipo de mapa que no caso de calor
        x = corr.columns,
        y = corr.index,
        z = np.array(corr),
        text=corr.values,
        texttemplate='%{text:.2f}',
        colorscale='ice'))

fig_heat.update_layout(
    height = 100,
    width = 100)

fig_heat.show()

fig_heat.write_html('grafico_calorrrr.html')


# Graficos Boxplot
vendas_regional = pd.read_excel("/Users/lucasarruda/Study/POS/Introdução Programação Python/(2) vendas_regiao.xlsx")

plt.figure(figsize=(15,9), dpi = 600)
sns.boxplot(data=vendas_regional, y='produtoA', width = 0.5, color = "lightblue")
plt.xlabel('Produto A',fontsize=15)
plt.ylabel('Valores',fontsize=15)
plt.show()

## Poderíamos fazer vários boxplot em um mesmo gráfico para comparacoes

var_boxplot = vendas_regional[['produtoA', 'produtoB', 'produtoC']]

plt.figure(figsize=(15,9), dpi = 600)
sns.boxplot(data=var_boxplot, width = 0.6, palette='rocket')
plt.xlabel('Produtos',fontsize=15)
plt.ylabel('Valores',fontsize=15)
plt.show()


## Torna-lo mais informativo
fig_box = px.box(var_boxplot,
                 width = 900)

fig_box.update_layout(title='BOXPLOT',
                      xaxis_title='Produtos',
                      yaxis_title='Valores',
                      plot_bgcolor='lightblue')

fig_box.update_traces(quartilemethod='inclusive') #uma escolha como ele calcula os quartis sendo inclusivo

fig_box.show()



#Pairplot 

sns.set_theme(rc={'figura'.dpi:100}) #o Pairplot vai mostrar histograma na diagonal, e escarteplots
sns.pairplot(data=atlas_ambiental.iloc[:[2,4,5]])
plt.show()