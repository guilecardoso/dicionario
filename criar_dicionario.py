import requests
from lxml import html
import pickle
import nltk

url = input("Digite a pagina com as palavras que deseja: ")
print(url)

caminho = input("Digite o xpath que está localizado na pagina: ")
print(caminho)

# caminho = "/html/body/div[2]/div/div[2]/div[3]/div/div[2]/p[4]/text()"

# url = "http://www.plainenglish.co.uk/campaigning/examples/long-sentences.html"

pagina = requests.get(url)

doc = html.fromstring(pagina.content)
valor = doc.xpath(caminho)

sentenca = valor[0]
print(sentenca)

tokens = nltk.word_tokenize(sentenca)

arquivo = open(b"palavras.obj","wb")
pickle.dump(tokens,arquivo)
arquivo.close()

print(tokens)