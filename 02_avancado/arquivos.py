# read(n), read(), readline(), readlines()

letra = open('caminho.arq', 'r')
print(letra.read(5)) # le 5 caracteres
print(letra.read()) # le todo o arquivo
print(letra.readline()) # le uma linha
print(letra.readlines()) # le todas as linhas

# contando as palavras
palavras = letra.read()
lista_palavras = palavras.split()
print(len(lista_palavras))
print(lista_palavras.count('I'))
set_palavras = set(lista_palavras) # remove as repetições
print(len(set_palavras))

letra.close() # fecha o arquivo

with open('text.txt', 'w') as file: # com o w começa no inicio do arquivo com o a começa no final
    file.write('Meu curso de python\n')
    file.write('Aqui na devSamurai\n')
