def main():
    # Calcule a soma dos numeros do 10 ao 14
    soma = sum(range(10, 15))
    print(soma) # 60
    
    # Calcule a media entre os numeros 10,15,20
    media = sum([10, 15, 20]) / 3
    print(media) # 15.0
    
    '''
      Peça para o usuario digitar duas notas de zero a dez e os pesos das notas e calcule a media ponderada
      exemplo: media = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
      Obs: lembrando que a soma dos pesos precisa ser dez
    '''
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    peso1 = float(input("Digite o peso da primeira nota: "))
    peso2 = float(input("Digite o peso da segunda nota: "))
    media = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
    print(media) # 10 10 5 5 == 10
    
    # Qual o menor preço desta lista de precos
    precos = [100.20, 34.90, 31.50, 18.95]
    menor_preco = min(precos)
    print(menor_preco) # 18.95
    
    # Avalie se o numero digitado pelo usuario é par ou impar
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        print("O numero é par") # par
    else:
        print("O numero é impar") # impar
        
    # Verifique se o menor preço dessa lista é menor que 20
    precos = [100.20, 34.90, 31.50, 18.95]
    menor_preco = min(precos)
    if menor_preco < 20:
        print("O menor preço é menor que 20") # menor que 20
    else:
        print("O menor preço é maior que 20") # maior que 20
    
    # Faça um programa que converta a temperatura em graus Fahrenheit fornecida pelo usuario em graus Celsius.
    # celsius = (fahrenheit - 32) * 5 / 9
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{celsius:2f}") # 37.77


if __name__ == '__main__':
    main()