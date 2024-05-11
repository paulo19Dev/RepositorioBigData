import numpy as np
import os
import pandas as pd
import plotly.express as px

#Arquivo de dados de 2024

lista_arquivo=pd.read_excel('teste.xlsx')
pd.set_option('display.max_rows', None)
display(lista_arquivo)

#quantidade de produtros vendidos

tabela_produtos=lista_arquivo.groupby('category').sum()
tabela_produtos=tabela_produtos[["description", "amount"]].sort_values(by= "amount" , ascending= False)
pd.set_option('display.max_rows', None)
display(tabela_produtos)

#categoria e produto que mais faturaram
lista_arquivo['price_total'] = lista_arquivo['amount'] * lista_arquivo['value_unit'] 
tabela_total = lista_arquivo.groupby('category').sum()
tabela_total=tabela_total[[ "price_total"]].sort_values(by= "price_total" , ascending= False)
pd.set_option('display.max_rows', None)
display(tabela_total)

#produtos que mais tiveram descontos
tabela_desconto=lista_arquivo.groupby('category').sum()
tabela_desconto=tabela_desconto[["preci_discount"]].sort_values(by= "preci_discount" , ascending= False)
pd.set_option('display.max_rows', None)
display(tabela_desconto)

#Grafico dos produtos mais vendidos
fig = px.line(tabela_produtos.reset_index(), x='category', y='amount',
             title='Produtos mais vendidos ',
             labels={'category': 'Categoria', 'amount': 'Total de produtos vendidos'})

fig.update_layout(xaxis_tickangle=-45, xaxis_title=None, yaxis_title='Total de produtos vendidos')

# Exiba o gráfico
fig.show()


#Graficos dos produtos com mais faturamento
fig = px.line(tabela_total.reset_index(), x='category', y='price_total',
             title='Produtos com mais faturamento por categoria',
             labels={'category': 'Categoria', 'price_total': 'Total de faturamentos'})

fig.update_layout(xaxis_tickangle=-45, xaxis_title=None, yaxis_title='Total de faturamentos')

# Exiba o gráfico
fig.show()


#Grafico dos produtos com descontos
fig = px.line(tabela_desconto.reset_index(), x='category', y='preci_discount',
             title='Produtos com mais descontos por categoria',
             labels={'category': 'Categoria', 'preci_discount': 'Total de descontos'})

fig.update_layout(xaxis_tickangle=-45, xaxis_title=None, yaxis_title='Total de descontos')

# Exiba o gráfico
fig.show()
