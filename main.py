from IPython.display import display
import pandas as pd



def format_price(value):
    # Formata o valor com ponto como separador de milhares e vírgula como separador decimal
    return '{:,.2f}'.format(value).replace(',', 'X').replace('.', ',').replace('X', '.')
# Caminho para o arquivo Excel
file_path = "relatorio.xlsx"

table = pd.read_excel(file_path)

#Contagem de produtos por categoria
category_counts = table['category'].value_counts()

#Criando coluna preço total que é a multiplicação do preço unitario de cada produto pela quantidade do produto
table["price_total"] = table['price_unit'] * table['amount']


#Calculando o valor de total de cada categoria e formando a forma em que aparece esse valor
total_price_by_category = table.groupby('category')['price_total'].sum()
# total_price_by_category = total_price_by_category.map(format_price)

categorys_table = pd.DataFrame({'Category': category_counts.index, 'Products Count': category_counts.values, "Price Total": total_price_by_category})



with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer: 
    categorys_table["Category"] = categorys_table["Category"].str.upper()
    
    categorys_table.to_excel(writer, sheet_name='categorys', index=False)
    table.to_excel(writer, sheet_name='products', index=False)
    
    

print("Nova tabela adicionada ao arquivo 'relatorio.xlsx'")
