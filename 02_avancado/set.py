# Set

cesta = {'maçã', 'banana', 'laranja', 'maçã'}
print(cesta)

contem = 'maçã' in cesta
print(contem)

palavra = set('abracadabra')
print(palavra)

a = {x for x  in 'abracadabra' if x not in 'abc'}
print(a)