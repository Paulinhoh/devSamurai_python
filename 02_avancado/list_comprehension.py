# List Comprehension
# uma sintaxe mais curta para criar uma lista baseado em uma lista já existente
# sintaxe: nova_lista = [expressão for item in interable if condicion == True]

animais = ['cachorro', 'gato', 'elefante', 'girafa', 'cavalo', 'zebra']
nova_lista = []

for animal in animais:
    if 't' in animal:
        nova_lista.append(animal)
print(nova_lista)

nova_lista2 = [animal for animal in animais if 't' in animal]
print(nova_lista2)

nova_lista3 = [numero for numero in range(10) if numero % 2 == 0]
print(nova_lista3)

nova_lista4 = [animal.upper() for animal in animais]
print(nova_lista4)

nova_lista5 = [animal if animal != 'cachorro' else 'macaco' for animal in animais]
print(nova_lista5)