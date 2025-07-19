import random

def main():
    numero_minimo = int(input("Digite o número mínimo do intervalo: "))
    numero_maximo = int(input("Digite o número maximo do intervalo: "))
    
    tentativas = int(input("Quantas tentativas para acertar? "))
    numero_sorteado = random.randint(numero_minimo, numero_maximo)
    
    while True:
        tentativa = int(input(f"Digite um número entre {numero_minimo} e {numero_maximo}: "))
        if tentativa == numero_sorteado:
            print("Você acertou!")
            break
        else:
            tentativas -= 1
            if tentativas == 0:
                print(f"Você perdeu! O numero era {numero_sorteado}")
                break
            else:
                print(f"Você errou! Você tem mais {tentativas} tentativas")


if __name__ == "__main__":
    main()