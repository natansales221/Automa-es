import pandas as pd
import numpy as np
import docx2txt
import os

def set_linha_df(df:pd.DataFrame, row) -> pd.DataFrame:
    insert_loc = df.index.max()
    
    if np.isnan(insert_loc):
        df.loc[0] = row
    else:
        df.loc[insert_loc +1] = row
    
    return df


diretorio = "C:/Users/natan/Desktop/Documentos"



for file in os.listdir(diretorio):
    if file.endswith(".docx"):
        df = pd.DataFrame([" "])
        caminho = os.path.join(diretorio, file)
        texto = docx2txt.process(caminho)
        linhas = texto.split("\n")
        for linha in linhas:
            if linha.strip() != "":
                df = set_linha_df(df, [str(linha)])
            if not os.path.exists(diretorio + "/processados"):
                os.mkdir(diretorio + "/processados")
            df.to_excel(diretorio + "/processados/" + file.replace(".docx", ".xlsx"), index=False)