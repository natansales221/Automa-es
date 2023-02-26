# Importações
import os
import pandas as pd
from sqlalchemy import create_engine

# Criando a conexão com o banco de dados MySQL usando o SQLAlchemy
engine = create_engine('mysql+mysqlconnector://root:123456@localhost/teste')

# Especificando o caminho para a pasta
path = 'xlsx'

for file_name in os.listdir(path):
    # Verificando se o item na pasta é um arquivo (e não uma pasta)
    if os.path.isfile(os.path.join(path, file_name)):
        if file_name[16:22] == "nomegenerico":
            df = pd.read_excel(os.path.join(path, file_name))
            # Inserindo os dados do dataframe na tabela do banco de dados MySQL
            df.to_sql(file_name[:29], con=engine, if_exists='replace', index=False)
            # Imprimindo uma mensagem informando que os dados foram inseridos com sucesso
            print(f"Dados de {file_name} inseridos com sucesso na tabela {file_name}")
        elif file_name[16:22] == "nomegenerico":
            df = pd.read_excel(os.path.join(path, file_name))
            # Inserindo os dados do dataframe na tabela do banco de dados MySQL
            df.to_sql(file_name[:28], con=engine, if_exists='replace', index=False)
            # Imprimindo uma mensagem informando que os dados foram inseridos com sucesso
            print(f"Dados de {file_name} inseridos com sucesso na tabela {file_name}")
        else:
            print("vai ser ignorada")

engine.dispose()