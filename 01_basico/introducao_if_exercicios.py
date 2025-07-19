def main():
    # Faça um programa que recebe do usuario duas notas de zero a dez, e escreve na tela você foi aprovado ou reprovado. Média 7.
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    if media >= 7:
        print('Você foi aprovado!')
    elif media >= 5 and media < 7:
        print('Você está de recuperação!')
    else:
        print('Você foi reprovado!')
        


if __name__ == '__main__':
    main()