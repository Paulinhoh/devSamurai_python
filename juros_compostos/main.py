from math import pow

def juros_compostos(capital, juros, tempo):
    return capital * pow(1 + juros, tempo)

def main():
    capital = float(input('Qual o capital de investimento? '))
    juros = float(input('Qual a taxa de juros anual em porcentagem (%)? ')) / 100
    temp = int (input('Quantos meses sera o investimento? ')) / 12
    
    valor_final_composto = juros_compostos(capital, juros, temp)
    print(f'O valor final do investimento é de R${valor_final_composto:.2f} R$')
    print(f'Os juros do rendimento foram de: {valor_final_composto - capital:.2f} R$')


if __name__ == '__main__':
    main()