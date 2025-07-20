# Dicionarios

empregados = {
    "01": {"João", "Silva"},
    "02": {"Maria", "Souza"},
    "03": {"Pedro", "Santos"}
}

print(type(empregados))
print(empregados)
print(empregados["01"])

empregados["04"] = {"Ana", "Silva"}

print(len(empregados))
print('01' in empregados)

del(empregados["01"])
print(empregados)

# numero_func = input("Digite o número do funcionário: ")
# nome = input("Digite o nome do funcionário: ")

# if empregados.get(numero_func) is not None:
#     print("Funcionário já cadastrado")
# else:
#     empregados[numero_func] = [nome] # type: ignore

print(empregados)

empregados.setdefault('01', ['Flavia']) # type: ignore
print(empregados)

empregados2 = {'06': ['Fulano', 'de Tal'], '07': ['Beltrano', 'da Silva']}
empregados.update(empregados2) # type: ignore
print(empregados)

# metodos uteis: keys(), values(), items()
dias = {'sex': 'sexta', 'seg': 'segunda', 'qua': 'quarta', 'qui':'quinta'}

chaves = dias.keys()
print(chaves,end='')

for chave in chaves:
    print(chave,end='')
    
valores = dias.values()
for value in valores:
    print(value,end='')

for item in dias.items():
    print(item)
    
dias.pop('sex')
print(dias)

# copias de dicionarios e listas

# dias_copy = dias
# dias_copy['sab'] = 'sabado'
# print(dias)

dias_copy = dias.copy()
dias_copy['sab'] = 'sabado'
print(dias)
print(dias_copy)