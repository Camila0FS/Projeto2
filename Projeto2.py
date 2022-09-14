# Programa 2 - criando planilhas 
# Descrição:
# Este programa criando planilhas dentro do arquivo orçamento.xls

# Autor: Camila Freitas Sant Ana
# Versão: 0.0.5 # Data: 13/09/2022

# Anotações: Planilhas: • receitas • despesas • resultados

# Abrir terminal - via jupiter notebook
# C:\Users\Users> cd projeto1
# C:\Users\Users\projeto1> ls (listou os arquivos)
# C:\Users\Users\projeto1> cd planilhas
# C:\Users\Users\projeto1\planilhas> ls (listou os arquivos)

# no jupiter notebook new ipykernel - renomeado Projeto2.py

# usando o pacote pacote openpyxl

from openpyxl import Workbook

wb = Workbook()

for planilha in ["receitas", "despesas", "resultado"]:
    wb.create_sheet(planilha)

wb.save("orcamento.xlsx")
