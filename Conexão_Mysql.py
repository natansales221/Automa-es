import mysql.connector

class connect_bd():

    def connect(self):
        con = mysql.connector.connect(host="localhost", database='teste', user='root', password='123456')

        cursor = con.cursor()

        resposta = int(input('Drop = 1, create = 2, insert = 3, select = 4 '))
        
        return resposta, cursor, con

    def apagar(self, resposta, cursor):

        if resposta == 1:
            try:
                cursor.execute('drop table cadastro')
                print("finalizado com sucesso")
            except:
                print("deu ruim")

    def criar(self, resposta, cursor):
        if resposta == 2:
            cursor.execute('create table if not exists cadastro ('
                        'id integer primary key auto_increment,'
                        'nome varchar(30),'
                        'login text,'
                        'senha text )')

            print("finalizado com sucesso")

    def inserir(self, resposta, cursor, con):
        if resposta == 3:
            try:
                cursor.execute("insert into cadastro (nome, login, senha)"
                            "values ('natan', 'gsrgeovanna', 'natan123')")
                con.commit()
                print("finalizado com sucesso")
            except:
                print("deu ruim")

    def selecionar(self, resposta, con):
        if resposta == 4:
            consulta_sql = "select * from cadastro"
            cursor = con.cursor()
            cursor.execute(consulta_sql)
            linhas = cursor.fetchall()
            for linha in linhas:
                print("Id:", linha[1])
                print("Nome:", linha[2])
                print("Sobrenome:", linha[3], "\n")
        con.commit()
        
    def main(self):
        conection = self.connect()
        
        if conection[0] == 1:
            self.apagar(resposta = conection[0], cursor = conection[1])
        elif conection[0] == 2:
            self.criar(resposta = conection[0], cursor = conection[1])
        elif conection[0] == 3:
            self.inserir(resposta = conection[0], cursor = conection[1], con = conection[2])
        elif conection[0] == 4:
            self.selecionar(resposta = conection[0], con = conection[2])

if __name__ == '__main__':
    service=connect_bd()
    service.main()
