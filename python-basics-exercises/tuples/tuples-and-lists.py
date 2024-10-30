""" tuple """
tupla = ('valor 1', 'valor 2', 'valor 3')

print(tupla[0])

print(tupla.index("valor 3"))

for valor in tupla:
    print(valor)

tupla2 = ('lorem', 'ipsum', 'dorem')

tupla3 = tupla + tupla2
print('tupla3', tupla3)

tupla4 = tupla * 2
print('tupla4', tupla4)

tuplaSlice = tupla[0:2]
print(tuplaSlice)

""" list """
listObj = ['valor 1', 'valor 2', 'valor 3']
listObj.append('valor 4')
print(listObj)

listObj.remove('valor 2')
print(listObj)

del(tupla3)
""" deleta a variavel selecionada """
