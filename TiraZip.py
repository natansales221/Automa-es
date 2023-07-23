import os
import zipfile
import pandas as pd

#diretorio do chromedriver
diretRaiz = r"diretorio"

# declarando o local de dowonload
diretorioFinal = "diretorio"
destino = "diretorio"
  
def TiraZip(): 
        # Verificando se a pasta de saída existe
    if not os.path.exists(destino):
        os.makedirs(destino)
        
    for arquivo in os.listdir(diretorioFinal):
        # Descompactando
        if arquivo.endswith('.zip'):
            with zipfile.ZipFile(diretorioFinal + "/" + arquivo) as zip_ref:
                # Agrupando na pasta
                zip_ref.extractall(destino)

    for file in os.listdir(destino):
        if file.endswith(".csv"):
            arqJunt = os.path.join(destino, file)
            df = pd.read_csv(arqJunt, encoding='ISO-8859-1', error_bad_lines=False, sep=";", index_col="CNPJ_FUNDO")

            newFile = os.path.join(destino, os.path.splitext(file)[0] + '.xlsx')
            df.to_excel(newFile, index=True)
