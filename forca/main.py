import random

def main():
    # cria uma lista de palavras que serão sorteadas
    palavras = ['abacaxi', 'banana', 'cachorro', 'dinheiro', 'elefante', 'futebol', 'gato', 'jogador', 'laranja', 'manga', 'notebook', 'ovo', 'pizza', 'queijo', 'rato', 'sapato', 'tenis', 'uva', 'ventilador', 'xadrez', 'zebra']
    
    # escolhemos uma das palavras da lista palavras
    palavra_sorteada = random.choice(palavras)
    
    # criamos uma sring com traços que representam as letras da palavra sorteada
    palavra_escondida = '-' * len(palavra_sorteada)
    
    # criamos uma lista com as letras que já foram adivinhadas
    letras_adivinhadas = []
    
    max_tentativas = 6
    
    while True:
        # mostras na tela a palavra escondida
        print(palavra_escondida)
        
        # pedimos para o usuário digitar uma letra
        letra = input('Digite uma letra: ')
        
        # verificamos se a letra já foi adivinhada
        if letra in letras_adivinhadas:
            print('Você já adivinhou essa letra!')
            continue
        
        # adicionar a letra na lista de letras adivinhadas
        letras_adivinhadas.append(letra)
        
        # verificar se a letra digitada está na palavra sorteada
        if letra in palavra_sorteada:
            lista = []
            for i in range(len(palavra_sorteada)):
                if palavra_sorteada[i] == letra:
                    lista.append(letra)
                else:
                    lista.append(palavra_escondida[i])
            palavra_escondida = ''.join(lista)
        else:
            max_tentativas -= 1
            print('Você errou!')
            print(f'Você ainda tem {max_tentativas} tentativas')
        
        # verificamos se o jogador ganhou uo perdeu
        if palavra_escondida == palavra_sorteada:
            print('Parabéns! Você ganhou!')
            break
        elif max_tentativas == 0:
            print(f'Você perdeu! A palavra era: {palavra_sorteada}')
            break


if __name__ == '__main__':
    main()