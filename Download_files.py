import zipfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import pandas as pd 



class downloadFiles():
    
    # Função para baixar os arquivos
    def download(self):

        diretorio =  r'C:\Users\natan\Desktop\Projetos\Automacoes'
        options = Options()
        # Fazendo com que nao abra janela
        options.add_argument("--headless")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--disable-notifications")
        options.add_argument('--no-sandbox')
        options.add_argument('--verbose')
        options.add_experimental_option("prefs", {
            "download.default_directory": diretorio,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
        })
        
        chromedriver_path = r'Automacoes\chromedriver-win64\chromedriver.exe'
        
        service = Service(executable_path=chromedriver_path)
        
        driver = webdriver.Chrome(service=service, options=options)
        try:
            # Baixando um arquivo teste
            driver.get('https://file-examples.com/index.php/sample-documents-download/sample-xls-download/')
            sleep(1.5)
            # Aceitando o cookie       
            link = driver.find_element(By.XPATH, '//*[@id="table-files"]/tbody/tr[1]/td[5]/a')
            link.click()
            sleep(5) 
            
            
            # Baixando um arquivo zip teste
            driver.get('https://file-examples.com/index.php/text-files-and-archives-download/')
            sleep(1.5)
            link = driver.find_element(By.XPATH, '//*[@id="table-files"]/tbody/tr[5]/td[5]/a')
            link.click()
        finally:
            driver.quit()
            
        return diretorio
          
    def agrupamento_csv(self):
        diretorio = self.download()
        # Encontrando o arquivo    
        # diretorio = "./"
        destino = diretorio + r"\csv"
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
    def agrupamento_xlsx(self):
        diretorio = self.download()
        destino = diretorio + r"\csv"
        destino = diretorio + r"\xlsx"
        # Verificando se a pasta de saída existe
        if not os.path.exists(destino):
            os.makedirs(destino)

        for file_name in os.listdir(diretorio):
            if file_name.endswith('.csv'):
                # Lendo o arquivo CSV e armazenar os dados em um dataframe
                input_file = os.path.join(diretorio, file_name)
                df = pd.read_csv(input_file, encoding='ISO-8859-1', error_bad_lines=False, sep=';')
                
                # Escrevendo os dados em um novo arquivo XLSX na pasta de saída
                output_file = os.path.join(diretorio, os.path.splitext(file_name)[0] + '.xlsx')
                df.to_excel(output_file, index=False)   
            
if __name__ == "__main__":
    service=downloadFiles()
    service.agrupamento_xlsx()