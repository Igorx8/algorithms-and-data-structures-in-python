coleta = {
    'Aedes aegypt': 32,
    'Aedes albopictus': 22,
    'Anopheles darlingi': 14
}

print(coleta['Aedes aegypt'])

coleta['Rhodnius montenegrensis'] = 11
print(coleta)

del(coleta)['Aedes albopictus']
print(coleta)

print(coleta.items())
print(coleta.keys())
print(coleta.values())

coleta2 = { 'Caninus espectrus': 13, 'Gatito pelito': 14}
coleta.update(coleta2)
print(coleta)

for especie, num_especimes in coleta.items():
    print(f"Espécie: {especie}, número de espécimes coletados: {num_especimes}")

biomoleculas = ('proteina', 'acidos', 'carbo', 'lipideo', 'carbo', 'carbo')

print(biomoleculas)

""" conjuntos (set) """
print(set(biomoleculas))

c1 = { 1,2,3,4,5 }
c2 = { 3,4,5,6,7 }
c3 = c1.intersection(c2)

print(c3)

print(c1.difference(c2))
print(c2.difference(c1))