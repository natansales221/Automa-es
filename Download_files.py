# Importações
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import zipfile
import os
import pandas as pd


# Função para baixar os arquivos
def download():
    fundo = 38
    driver = webdriver.Chrome()
    while fundo < 51:
        # Acessando o site
        driver.get('www.google.com/sitegenerico')
        sleep(1.5)
        # Baixando arquivos
        link = driver.find_element(By.XPATH, 'xpath generica' + str(fundo) + ']')
        link.click()
        fundo +=1
    sleep(3)
    driver.quit()

# Função para tirar do zip    
def agrupamento_csv():
    # Encontrando o arquivo    
    diretorio = "./"
    destino = "csv"
    # Verificando se a pasta de saída existe
    if not os.path.exists(destino):
        os.makedirs(destino)
        
    for arquivo in os.listdir(diretorio):
        caminho = os.path.join(diretorio, arquivo)
        # Descompactando
        if os.path.isfile(caminho) and arquivo.endswith('.zip'):
            with zipfile.ZipFile(caminho, 'r') as zip_ref:
                # Agrupando na pasta
                zip_ref.extractall(destino)

# Função para transformar em xlsx               
def agrupamento_xlsx():
    input_folder = "./csv"
    output_folder = "./xlsx"
    # Verificando se a pasta de saída existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.csv'):
            # Lendo o arquivo CSV e armazenar os dados em um dataframe
            input_file = os.path.join(input_folder, file_name)
            df = pd.read_csv(input_file, encoding='ISO-8859-1', error_bad_lines=False, sep=';', index_col='CNPJ_FUNDO')
            
            # Escrevendo os dados em um novo arquivo XLSX na pasta de saída
            output_file = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.xlsx')
            df.to_excel(output_file, index=True)   
        
download()
agrupamento_csv()
agrupamento_xlsx()