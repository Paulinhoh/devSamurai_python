def main():
    temperatura = int(input('Digite a temperatura: '))
    if temperatura > 25:
        print('Calor')
    elif temperatura < 15:
        print('Frio')
    else:
        print('Normal')


if __name__ == '__main__':
    main()