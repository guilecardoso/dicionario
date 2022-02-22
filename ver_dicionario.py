import pickle

arquivo = open("palavras.obj","rb")
obj = pickle.load(arquivo)
for tudo in obj:
	print(tudo)

arquivo.close()