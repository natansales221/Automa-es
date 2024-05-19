import pandas as pd
import numpy as np
import docx2txt
import os

class wordToExcel():

    def set_linha_df(df:pd.DataFrame, row) -> pd.DataFrame:
        insert_loc = df.index.max()
        
        if np.isnan(insert_loc):
            df.loc[0] = row
        else:
            df.loc[insert_loc +1] = row
        
        return df

    @property
    def diretorio(self):
        return{
            'diretorio':"C:/Users/natan/Desktop/Documentos"}
        


    def docx_to_excel(self):
        for file in os.listdir(self.diretorio['diretorio']):
            if file.endswith(".docx"):
                df = pd.DataFrame([" "])
                caminho = os.path.join(self.diretorio['diretorio'], file)
                texto = docx2txt.process(caminho)
                linhas = texto.split("\n")
                for linha in linhas:
                    if linha.strip() != "":
                        df = self.set_linha_df(df, [str(linha)])
                    if not os.path.exists(self.diretorio['diretorio'] + "/processados"):
                        os.mkdir(self.diretorio['diretorio'] + "/processados")
                    df.to_excel(self.diretorio['diretorio'] + "/processados/" + file.replace(".docx", ".xlsx"), index=False)
                    
if __name__ == '__main__':
    service=wordToExcel()
    service.docx_to_excel
                    
    