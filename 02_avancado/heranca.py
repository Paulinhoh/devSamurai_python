# herança = um novo objeto ira herdar as caracteristicas do objeto pai

class Empregado:
    def __init__(self, nome, identificacao):
        self.nome = nome
        self.identificacao = identificacao
        
    def registrar_ponto(self):
        print('Registrando o ponto')
        
    # sobreescreve e retorna as caracteristicas do objeto
    def __str__(self) -> str:
        return f'{self.identificacao} do empregado {self.nome}'


class corpoDocente(Empregado):
    def __init__(self, nome, identificacao, diciplina):
        super().__init__(nome, identificacao)
        self.diciplina = diciplina
    
    def atribuir_notas(self, nota):
        print(f'Atribuindo nota {nota}')


class Administrativo(Empregado):
    def __init__(self, nome, identificacao, setor):
        super().__init__(nome, identificacao)
        self.setor = setor

    def atribuir_tarefas(self, tarefa):
        print(f'Atribuindo tarefa {tarefa}')


empregado = Empregado('João', '123456')
print(empregado)

professor = corpoDocente('Maria', '123457',  'Matemática')
professor.atribuir_notas(10)

secretario = Administrativo('João', '123458', 'Financeiro')
secretario.atribuir_tarefas('Fazer relatório')
print(secretario.setor)