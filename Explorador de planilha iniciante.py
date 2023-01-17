import pandas as pd

plani = pd.read_excel('./teste.xlsx')

table = str(input("qual o nome da tabela que voce quer adicionar? "))

plani[table.upper()] = plani['ID'] * (4)
plani.dropna(how='all')
print(plani)