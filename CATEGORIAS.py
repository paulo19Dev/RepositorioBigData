O código que fiz cria uma página chamada "quantidade" dentro da planilha, se você achar melhor posso trocar de página para nova planilha.

Código:

import openpyxl
import pandas as pd

# Carrega o arquivo Excel
file_name = " "  # Nome do arquivo
sheet_name = " "  # Nome da planilha
df = pd.read_excel(file_name, sheet_name=sheet_name)

# Verifica as categorias de produtos na coluna "type" e conta a quantidade de produtos presentes em cada uma
category_counts = df['type'].value_counts()

# Abre o arquivo Excel
workbook = openpyxl.load_workbook(file_name)

# Adiciona os dados de quantidade em uma nova página na planilha
new_sheet_name = "quantidade"
new_sheet = workbook.create_sheet(title=new_sheet_name)

# Adiciona os cabeçalhos
new_sheet['A1'] = "Categoria"
new_sheet['B1'] = "Quantidade"

# Adiciona os dados de quantidade
for i, (category, count) in enumerate(category_counts.items(), start=2):
    new_sheet[f'A{i}'] = category
    new_sheet[f'B{i}'] = count

# Salva as modificações no arquivo Excel
workbook.save(file_name)
print(f"Dados de quantidade adicionados com sucesso na pagina '{new_sheet_name}' do arquivo '{file_name}'")
