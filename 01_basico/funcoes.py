# Função sem retorno e passagem de parametro
def ola_mundo():
    # função que mostra uma mensagem padrão na tela
    print('Olá Mundo')
    
# Função sem retorno e com passagem de parametro
def ola_mundo_nome(nome='User'):
    # função que mostra um texto personalizado na tela
    print(f'Olá Mundo, meu nome é {nome}')
    
# Função com retorno e passagem de parametro
def somar(a=0, b=0):
    # função que retorna um texto personalizado na tela
    return a + b

def main():
    help(ola_mundo)
    ola_mundo()
    ola_mundo_nome('Paulinho')
    soma = somar(5, 7)
    print(soma)


if __name__ == '__main__':
    main()