import os

dire = r'C:\Users\natan.sales\Desktop\teste\deletar'

for file in os.listdir(dire):
    caminho = os.path.join(dire, file)
    if os.path.isfile(caminho):
        os.remove(caminho)