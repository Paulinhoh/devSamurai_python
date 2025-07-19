def main():
    animais = ['cachorro', 'gato', 'elefante']
    print(type(animais))
    
    print(animais[0])
    print(animais[1])
    print(animais[2])
    print(animais[-1])
    
    print(len(animais))
    
    mais_animais = ['leão', 'tigre', 'urso']
    soma_listas = animais + mais_animais
    print(soma_listas)
    
    print('pato' in soma_listas) # false
    print('leão' in soma_listas) # true
    
    diversas = ['string', 7, True, 3.1415]
    print(diversas)
    
    valores = [10,40,25,82,33]
    print(min(valores))
    print(max(valores))
    print(sum(valores))
    
    # funções biult-in
    mercado = ['cebola', 'alho', 'macarrão']
    mercado.append('tomate')
    mercado.count('cebola')
    mercado.index('tomate')
    mercado.insert(1, 'abacate')
    
    mercado.sort()
    mercado.sort(reverse=True)
    mercado.reverse()
    
    mercado.pop(1)
    mercado.remove('alho')

    # listas são multaveis
    lista = ['cachorro', 'gato']
    lista[0] = 'elefante'
    print(lista)


if __name__ == '__main__':
    main()