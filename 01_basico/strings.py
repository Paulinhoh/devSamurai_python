def main():
    s = "Sou uma string"
    print(type(s))
    
    s = 'olá '
    t = 'mundo'
    print(s + t) # concatenação de strings
    
    print("-" * 3)

    print('m' in t) # true
    print('M' in t) # false
    print(len(t))
    
    # Indexação de strings
    msg = 'Curso de python'
    print(msg[0])
    print(len(msg))
    nova_msg = msg[0:5]
    print(nova_msg)
    
    print(msg[-1])
    
    # Funções built-in de strings
    print(msg.count('o'))
    print(msg.upper())
    print(msg.lower())
    print(msg.capitalize())
    print(msg.title())
    print(msg.replace('python', 'Java'))
    print(msg.split())
    print(msg.split('o'))
    print(msg.strip())


if __name__ == '__main__':
    main()