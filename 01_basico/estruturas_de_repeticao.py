def main():
    # while
    numero = 0
    while numero <= 10:
        print(numero, end='')
        numero += 1 # numero = numero + 1
    print('Fim do while')
    
    # for
    for dia in ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']:
        print(dia, end='')
        
    for numero in range(0,11):
        print(numero, end='')
    
    


if __name__ == '__main__':
    main()