import pandas as pd
from bs4 import BeautifulSoup

with open("C:/Users/natan.sales/Downloads/arquivos teste/Politica de Compliance - v008.html", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

diretorio = 'C:/Users/natan.sales/Downloads/arquivos teste/'

df = pd.DataFrame(["coluna1"])

for linha in soup.find_all('p'):
    df = (df, [str(linha)])

df.to_excel(diretorio + 'teste.xlsx', index=False)
