while True:
    try:
        x = int(input('Digite um número: '))
        break
    except ValueError:
        print('Você não digitou um número')
        
print(f'O numero digitado foi: {x}')