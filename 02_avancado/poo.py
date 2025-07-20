class Pessoa():
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        
    def andar(self):
        print(f'{self.nome} está andando')
    
    def falar(self):
        print(f'{self.nome} está falando')
    
    def comer(self):
        print(f'{self.nome} está comendo')

    def dormir(self):
        print(f'{self.nome} está dormindo')
        
    def imc(self):
        return self.peso / (self.altura ** 2)
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, valor):
        if valor < 0:
            raise ValueError('Altura não pode ser menor que 0')
        elif isinstance(valor, str):
            valor = float(valor)
        self._altura = valor


pessoa1 = Pessoa('Paulinho', 23, 1.80, 60)
pessoa2 = Pessoa('Flavia', 20, 1.65, 50)

print(pessoa1.altura)
print(pessoa2.altura)

pessoa2.falar()
pessoa1.dormir()
