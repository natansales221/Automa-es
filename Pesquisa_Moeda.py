import requests
from bs4 import BeautifulSoup


def dolar():
    try:
        response = requests.get('https://www.remessaonline.com.br/cotacao/cotacao-dolar')
        site = BeautifulSoup(response.content, 'html.parser')
        cotacao = site.find('div', {'class': 'style__Text-sc-1a6mtr6-2 ljisZu'}).text[0:4]
        print(print("a cotação do dolar, atualmente está em {}" .format(cotacao)))
    except:
        print('deu faia')



def euro():
    try:
        response = requests.get('https://www.remessaonline.com.br/cotacao/cotacao-euro')
        site = BeautifulSoup(response.content, 'html.parser')
        cotacao = site.find('div', {'class': 'style__Text-sc-1a6mtr6-2 ljisZu'}).text[0:4]
        print("a cotação do euro, atualmente está em {}" .format(cotacao))
    except:
        print('deu faia')


dolar()
euro()
