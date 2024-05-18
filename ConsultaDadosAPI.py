import os
import json
import requests
import pandas as pd

from time import sleep




class consulta_cpf():
    @property
    def dados(self):
        return {
            'parquet_id_dir': r'diretorio',
            'headers': {'Content-type': 'application/json', "Authorization":"Bearer"},
            'caminho': r'diretorio'
            }
        

    def leitura(self):

        for a in os.listdir(self.dados['caminho']):
           df_read = pd.read_excel(self.dados['caminho'] + '\\' + a, engine='openpyxl')
        
        request = requests.post("diretorio", headers=self.dados['headers'], data=json.dumps("credenciais"))
        self.dados['headers']['Authorization'] = 'Bearer ' + request.json()['access_token']
        
        for b, id in enumerate(df_read['RESULTADO']):
            if pd.isna(df_read['status'].iloc[b]):
                if df_read['status'].where(df_read['RESULTADO'] == id)[b] != 'ok':     
                    url = "status"
                    chamada = requests.get(url + id + 'paginacao_querystring', headers=self.dados['headers'])
                    chamada = chamada.json()
                    if 'message' in chamada:
                        request = requests.post("diretorio", headers=self.dados['headers'], data=json.dumps("credenciais"))
                        self.dados['headers']['Authorization'] = 'Bearer ' + request.json()['access_token']
                        chamada = requests.get(url + id + 'paginacao_querystring', headers=self.dados['headers'])
                        chamada = chamada.json()
                        pass
                    if 'data' in chamada:
                        df = pd.DataFrame(chamada['data'][0]['resultados'])
                        # df.to_excel(caminho + f"\\teste{b}.xlsx", index=False)
                        df = []
                        df_read.loc[df_read['RESULTADO'] == id, 'status'] = 'ok'
                        
                        if (b+1) % 10 == 0:
                            sleep(60)
                else:
                    pass
        df_read.to_excel(self.dados['caminho'] + f"\\teste{b}.xlsx", index=False)
                
    def result(self):
    # For de arquivo da pasta, sendo i o número do arquivo
        for i, file in enumerate(os.listdir(self.dados['parquet_id_dir'])):

            # Lendo arquivo por arquivo
            df = pd.read_excel(self.dados['parquet_id_dir'] + "\\" + file, engine="openpyxl")
            id_list = df['RESULTADO']
            result = []

            # For de item por coluna, sendo E o número da linha
            for e, id in enumerate(id_list):
                url = "url_api"
                chamada = requests.get(url + id + 'paginacao_querystring', headers=self.dados['headers'])
                chamada = chamada.json()

                # Validando se há dados para armazenamento
                if 'data' in chamada:
                    a = pd.DataFrame(chamada['data'][0]['RESULTADO'])
                    a.to_excel(self.dados['caminho'] + f"\\teste{i, e}.xlsx", index=False)
                    a = []
                else:
                    print(chamada)       

if __name__ == '__main__':
    service=consulta_cpf()
    service.leitura()