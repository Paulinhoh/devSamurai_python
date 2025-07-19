def main():
    # Faça um programa que gere uma tabela de multiplicação de um número qualquer. O programa deve pedir para o usuário digitar o número que deseja ver a tabuada.
    numero = int(input('Digite um número: '))
    limite = int(input('Digite o limite da tabuada: '))
    
    for i in range(0,limite + 1):
        print(f'{numero} x {i} = {numero * i}')
    
    
    # Faça um programa que calcule o enesimo termo da sequência de Fibonacci. Lembrando que a série começa da seguinte forma: 1,1,2,3,5,8
    enesimo_termo = int(input('Digite qual elemento da serie deve ser mostrado: '))
    primeiro = 1
    segundo = 1
    
    if (enesimo_termo == 1 or enesimo_termo == 2):
        print(1)
    else:
        for _ in range(2,enesimo_termo):
            elemento = primeiro + segundo
            primeiro = segundo
            segundo = elemento
        print(elemento) # type: ignore


if __name__ == '__main__':
    main()