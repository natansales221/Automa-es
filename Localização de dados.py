import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


URL = 'https://app.anm.gov.br/DadosAbertos/ARRECADACAO/CFEM_Arrecadacao.csv'
r = requests.get(URL, allow_redirects=True)
file_name = URL.split('/')[-1]
with open(file_name, 'wb') as f:
    f.write(r.content)    
    
def le_dados(filename):
    with open(filename, 'r', encoding='ISO-8859-1') as file:
    
        # Criando uma lista vazia para armazenar todos os dados do arquivo
        dados = []

        # remove o caractere '\n' do final da linha
        # transforma a linha em uma lista
        for line in file:
            dados.append(line.rstrip().replace('","','";"').replace('"','').split(';'))
            dados[-1][-3] = dados[-1][-3].replace(',','.')
            dados[-1][-1] = dados[-1][-1].replace(',','.')
        
    # Separando a primeira linha do arquivo para uma lista separada de 'rotulos'
    rotulos = dados.pop(0)
    
    return rotulos, dados

############# BLOCO PRINCIPAL DO PROGRAMA #############
rotulos, dados = le_dados("CFEM_Arrecadacao.csv")

print (rotulos, '\n')
print (dados[0])
print ("Número total de registros: %d" % (len(dados)))
print()

# Criando dicionario pra facilitar acesso aos registros
index = 0
reg = {}
for d in rotulos:
  reg[d] = index
  index=index+1
print(reg)
