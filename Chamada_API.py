import os
import json
import requests
import pandas as pd

from datetime import datetime


class consulta_cpf():

    @property
    def caminhos_cloud(self):
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
    def caminhos_site(self):
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
       
        r = requests.post(self.caminhos_site[0]["url_token"], headers=headers, data=json.dumps())
        return r       

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

            self.log.info("lendo os arquivos para fazer comparativo")

            df_controle = pd.read_csv(self.caminhos_site[0]['nome_camimho'], delimiter=';')
            dt_controle = datetime.strptime(df_controle['endereço'][0], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')

            df_file = pd.read_csv(self.caminhos_site[0]['nome_camimho'], delimiter=';')
            df_file['endereço'] = df_file['endereço'].str.replace('-', '').str.replace('/', '').str.replace('.', '')
            df_file = df_file['endereço']

            
            df_certo = df_erro = df_sem_result = pd.DataFrame()
            self.log.info("Arquivos lidos! Iniciando processamento")
            r = self.token()

            for a, data in enumerate(df_file):
                if pd.isna(data):
                        pass
                else:
                    if data < dt_controle:
                        if r.status_code == 200:
                            if pd.isna(df_file.loc[a, 'telefone']):

                                if df_file['telefone'].notnull().any():
                                    a+=1
                                    pass
                            else:
                                id = df_file['telefone'].values[a]
                                params['params']['telefone'] = str(df_file['telefone'].values[a])

                                if id in lista_falha:
                                    a+=1
                                    pass

                                else:

                                    if r.status_code == 200:
                                        headers = {'Content-type': 'application/json', "Authorization":""}
                                        s_body = r.json()
                                        
                                        #chamada de api realizada com sucesso
                                        # se faz necessária a mudança dos links para confirmação
                                        headers['Authorization'] = 'Bearer ' + r.json()['access_token']
                                        r_t = requests.post(self.caminhos_site[0]["url_api"], headers=headers, data=json.dumps(params))

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
                                        self.log.info("Erro {}: {}".format(r.status_code, status))
                                        a+=1

                        elif r.status_code == 401:
                            r = self.token()
                            pass
                    else:

                        self.log.info('Não pesquisa')
                        a+=1
            
            self.log.info("Salvando na pasta!")

            df_final = pd.concat([df_sem_result, df_erro, df_certo], axis=0, ignore_index=True)
            df_final.rename(columns=self.colunas, inplace=True)

           

        except Exception as e:
            raise Exception("Error. ", e)


if __name__ == '__main__':
    service=consulta_cpf(True)
    service.teste_token()
