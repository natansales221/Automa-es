import os

class delete():
    
    @property
    def diretorio(self):
        return{
            'diretorio': r'C:\Users\natan\Desktop\teste\deletar'
        }
    def apaga_tudo(self):
        for file in os.listdir(self.diretorio['diretorio']):
            caminho = os.path.join(self.diretorio['diretorio'], file)
            if os.path.isfile(caminho):
                os.remove(caminho)
                print(file, " apagado com sucesso")
            
if __name__ == '__main__':
    service=delete()
    service.apaga_tudo()