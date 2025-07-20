# uma função lambda é uma pequena função anônima
# recebe os argumentos porem só pode executar uma expressão
# lambda argumentos: expressão

x = lambda a: a * 3
print(x(2))

soma = lambda a, b: a + b
print(soma(3, 5))

graus_celsius = lambda c: (5/9) * (c-32)
print(graus_celsius(32))