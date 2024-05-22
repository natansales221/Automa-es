import os
import pandas as pd
import urllib.request
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


cdrive = r'diretorio'
caminho = r'diretorio'
options = Options()
driver = webdriver.Chrome(executable_path=cdrive, options=options)
filename = "filename.csv"
txt_file = "filename.txt"

dict_comparativa = {'filename.csv': '19-04-2023 09:34', 'filename.txt': '20-04-2023 09:34'}

class download():
    
    def extracao_dados_site(self):
        global info, data_csv, hora_csv, data_txt, hora_txt
        
        driver.get("link")
        # Extração de informações sobre o arquivo csv (data e hora da ultima atualização)
        data_csv = datetime.strptime(driver.find_element(By.CSS_SELECTOR, 'pre').text.splitlines()[2].split()[1], '%d-%b-%Y').strftime('%d-%m-%Y')
        hora_csv = driver.find_element(By.CSS_SELECTOR, 'pre').text.splitlines()[2].split()[2]
        
        driver.get("link")
        # Extração de informações sobre o arquivo txt (data e hora da ultima atualização)
        data_txt = datetime.strptime(driver.find_element(By.CSS_SELECTOR, 'pre').text.splitlines()[1].split()[1], '%d-%b-%Y').strftime('%d-%m-%Y')
        hora_txt = driver.find_element(By.CSS_SELECTOR, 'pre').text.splitlines()[1].split()[2]
        
        info = {f"{filename}": f"{data_csv} {hora_csv}", f"{txt_file}": f"{data_txt} {hora_txt}"}
        print("as informações baixadas do site são as {}".format(info))

    def download_csv(self):     
        # Download do arquivo csv
        driver.get("link")
        down_csv = driver.find_element(By.XPATH, "/html/body/div[1]/pre/a[3]")
        urllib.request.urlretrieve(down_csv.get_attribute("href"), filename)

    def download_txt(self):
        # Download do arquivo txt
        txt = "link"
        urllib.request.urlretrieve(txt, txt_file)

    def validacao_csv(self):
        service.extracao_dados_site()
        if (dict_comparativa['filename.csv'] < info['filename.csv']) & (dict_comparativa['filename.txt'] < info['filename.txt']) :
            service.download_cad_fi_csv()
            service.download_cad_fi_txt()
            
            # Extraindo a data que o arquivo está rodando
            data = datetime.now().strftime('%d-%m-%Y %H.%M')
            
            # Criação da pasta que o arquivo ficará
            new_folder = os.path.join(caminho, data)
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)

            # Salvando na pasta
            os.replace(filename, os.path.join(new_folder, filename))
            os.replace(txt_file, os.path.join(new_folder, txt_file))
            
            # Criando o Dataframe
            dados = f"{filename} | {data_csv} {hora_csv} | {data}\n {txt_file} | {data_txt} {hora_txt} | {data}"

            # Conversão de string em uma lista de listas
            data_list = [row.split(" | ") for row in dados.split("\n")]

            # Criação do dataframe e salvar em CSV
            df = pd.DataFrame(data_list, columns=["nm_arquivo", "dt_modificacao", "dt_carga"])
            df.to_csv(new_folder + "\\filename.csv", index=False)  
            
        else:
            print("nao vai baixar")
    

if __name__ == '__main__':
    service=download(True)
    service.validacao_csv()