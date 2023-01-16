try:
    import mysql.connector
except:
    print("VOCE PRECISA IMPORTAR AS BIBLIOTECAS")

con = mysql.connector.connect(host="localhost", database='teste', user='root', password='123456')

cursor = con.cursor()

r = int(input('Drop = 1, create = 2, insert = 3, select = 4 '))


def apagar():
    if r == 1:
        try:
            cursor.execute('drop table cadastro')
            print("finalizado com sucesso")
        except:
            print("deu ruim")

def criar():
    if r == 2:
        cursor.execute('create table if not exists cadastro ('
                       'id integer primary key auto_increment,'
                       'nome varchar(30),'
                       'login text,'
                       'senha text )')

        print("finalizado com sucesso")

def inserir():
    if r == 3:
        try:
            cursor.execute("insert into cadastro (nome, login, senha)"
                           "values ('natan', 'gsrgeovanna', 'natan123')")
            con.commit()
            print("finalizado com sucesso")
        except:
            print("deu ruim")

def selecionar():
    if r == 4:
        consulta_sql = "select * from cadastro"
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        for linha in linhas:
            print("Id:", linha[1])
            print("Nome:", linha[2])
            print("Sobrenome:", linha[3], "\n")
    con.commit()

if r == 1:
    apagar()
elif r == 2:
    criar()
elif r == 3:
    inserir()
elif r == 4:
    selecionar()

