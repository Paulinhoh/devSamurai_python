'''
    Variaveis
    
    * variaveis são lugares de memoria que irão armazenar um dado
    * <nome da variavel> = <dado ou expressão>
    * seu nome pode conter letras, numeros, e _
    * não pode começar com numero, nem conter espaços
    * sempre dar um nome significativo, por exemplo item é melhor que apenas i
    * para nomes com mais de uma palavra, separe-as com _ ou use camelCase ex.: (nome_completo, nomeCompleto)
    * evite nomes muito longos
'''

def main():
    x:int = 7
    print(x + 3) # 10
    
    var_temp:int = 38
    
    y = x + 8
    print(y) # 15


if __name__ == '__main__':
    main()