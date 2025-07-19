def main():
    # Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
    numero = int(input('Digite um número inteiro: '))
    fatorial = 1
    while numero > 0:
        fatorial *= numero
        numero -= 1
    print(f'O fatorial de número digitado é {fatorial}')
    
    # Vamos fazer um programa que simule um cofre. Ele tera uma senha predefinida e o usuario tera 3 chances para acertar a senha. A cada tentativa errada devera mostrar a mensagem "Senha incorreta, tente novamente"". Caso o usuario acerte a senha, o programa deve mostrar a mensagem "Acesso permitido" e encerrar.
    senha = '1234'
    tentativas = 3
    
    while tentativas > 0:
        senha_digitada = input('Digite a senha: ')
        if senha_digitada == senha:
            print('Acesso permitido')
            break
        else:
            print('Senha incorreta, tente novamente')
            tentativas -= 1
    
    if tentativas > 0:
        print('Cofre aberto')
    else:
        print('Cofre trancado')


if __name__ == '__main__':
    main()