def quadrado(num=5):
    return num ** 2

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def quadrado_ou_cubo(palavra, numero):
    if palavra == 'quadrado':
        return numero ** 2
    elif palavra == 'cubo':
        return numero ** 3


def main():
    # escreva uma função que calcule o quadrado do numero passado como parametro. Se nenhum numero for passado, calcule o quadrado de 5.
    quadrado(7)
    
    # escreva uma função que receba como parametro uma temperatura em graus Fahrenheit e retorne o valor em graus Celsius.
    fahrenheit_para_celsius(100)
    
    # escreva uma função que receba dois parametros. O primeiro sera uma palavra, se ela for quadrado devera calcular o quadrado do numero passado como segundo parametro. Se a palavra for cubo devera calcular o cubo do numero passado.
    quadrado_ou_cubo('cubo', 5)

if __name__ == '__main__':
    main()