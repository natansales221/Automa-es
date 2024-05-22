import os
import json
import requests
import pandas as pd

from datetime import datetime


class consulta_cpf():

    @property
    def caminho_do_upload(self):
        return [
            {
                "nome_camimho": "caminho_do_arquivo",
                "nome_camimho": "caminho_do_arquivo",
                "nome_camimho": "caminho_do_arquivo",
                "nome_camimho": "caminho_do_arquivo",
                "nome_camimho": "caminho_do_arquivo",
                }
        ]

    @property
    def caminho_da_pesquisa(self):
        return [
            {
                "nome_camimho": "url_site",
                "nome_camimho": "url_site",
                "nome_camimho": "url_site",
                "nome_camimho": "url_site",
            }
        ]


    def token(self): 
        headers = {'Content-type': 'application/json', "Authorization":""}
       
        requests = requests.post(self.caminho_da_pesquisa[0]["url_token"], headers=headers, data=json.dumps())
        return requests
    
    def colunas(self):
        {
                'id': [''],
                'nome': [''],
                'cpf': [''],
                'endereço': [''],
                'telefone': [''],
                'rg': [''],
                'tipo_sanguineo': [''],
                'comida_preferida': [''],
        }
        
    def teste_token(self):
        try:
            
            hoje = datetime.now().strftime('%d-%m-%Y')
            lista_falha = lista_nao_encontra = []
            params = {
                "params": {
                "document":"",
                "ano":"2022"} }
            
            dataframe_base = {
                'id': [''],
                'nome': [''],
                'cpf': [''],
                'endereço': [''],
                'telefone': [''],
                'rg': [''],
                'tipo_sanguineo': [''],
                'comida_preferida': [''],
            }

            print("lendo os arquivos para fazer comparativo")

            dataframe_do_nome = pd.read_csv(self.caminho_da_pesquisa[0]['nome_camimho'], delimiter=';')
            str_data = datetime.strptime(dataframe_do_nome['endereço'][0], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')

            dataframe = pd.read_csv(self.caminho_da_pesquisa[0]['nome_camimho'], delimiter=';')
            dataframe['endereço'] = dataframe['endereço'].str.replace('-', '').str.replace('/', '').str.replace('.', '')
            dataframe = dataframe['endereço']

            
            df_certo = df_erro = df_sem_result = pd.DataFrame()
            print("Arquivos lidos! Iniciando processamento")
            token = self.token()

            for a, data in enumerate(dataframe):
                if pd.isna(data):
                    pass
                else:
                    if data < str_data:
                        if token.status_code == 200:
                            if pd.isna(dataframe.loc[a, 'telefone']):

                                if dataframe['telefone'].notnull().any():
                                    a+=1
                                    pass
                            else:
                                id = dataframe['telefone'].values[a]
                                params['params']['telefone'] = str(dataframe['telefone'].values[a])

                                if id in lista_falha:
                                    a+=1
                                    pass

                                else:

                                    if token.status_code == 200:
                                        headers = {'Content-type': 'application/json', "Authorization":""}
                                        s_body = token.json()
                                        
                                        #chamada de api realizada com sucesso
                                        # se faz necessária a mudança dos links para confirmação
                                        headers['Authorization'] = 'Bearer ' + token.json()['access_token']
                                        r_t = requests.post(self.caminho_da_pesquisa[0]["url_api"], headers=headers, data=json.dumps(params))

                                        if r_t.status_code == 500:
                                            self.token()
                                            pass
                                        
                                        if r_t.status_code == 200:
                                            r_t = r_t.json()

                                            if ('message' in r_t) | (r_t['data'] == None):

                                                dataframe_base['nome'] = r_t['message']
                                                dataframe_base['nome'] = id
                                                dataframe_base['nome'] = hoje
                                                df_ne = pd.DataFrame(dataframe_base)
                                                df_sem_result = df_sem_result.append(df_ne)
                                                print(a, "sem resultado")
                                                lista_nao_encontra.append(id)
                                                a+=1

                                            else:

                                                empresa = r_t['data']
                                                socios = r_t['data']['nome']
                                                df2 = pd.DataFrame(empresa)
                                                df2 = df2.drop(df2.columns[3], axis=1)
                                                df2 = df2.rename(columns={'nome': 'nome'})
                                                df3 = pd.DataFrame(socios)
                                                df4 = pd.concat([df2, df3], axis=1)
                                                df4['dt_modificacao'] = hoje
                                                df_certo = df_certo.append(df4)
                                                df_certo['status'] = 'OK'
                                                print(a, "deu certo")
                                                a+=1

                                        
                                        else:

                                            dataframe_base['nome'] = r_t.text
                                            dataframe_base['nome'] = id
                                            dataframe_base['nome'] = hoje
                                            df_f = pd.DataFrame(dataframe_base)
                                            df_erro = df_erro.append(df_f)
                                            lista_falha.append(id)
                                            print(a, "falhou")
                                            a+=1
                                            pass
                                    
                                    else:

                                        status = s_body['nome']
                                        print("Erro {}: {}".format(token.status_code, status))
                                        a+=1

                        elif token.status_code == 401:
                            token = self.token()
                            pass
                    else:

                        print('Não pesquisa')
                        a+=1
            
            print("Salvando na pasta!")

            df_final = pd.concat([df_sem_result, df_erro, df_certo], axis=0, ignore_index=True)
            df_final.rename(columns=self.colunas, inplace=True)

           

        except Exception as e:
            raise Exception("Error. ", e)


if __name__ == '__main__':
    service=consulta_cpf(True)
    service.teste_token()
