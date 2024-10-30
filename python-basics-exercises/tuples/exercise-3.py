import numpy as np

""" exercicio 1 """
somaLista = 0
tamanhoLista = 5

lista = []

for numero in range(0, tamanhoLista):
    lista.append(int(input('Digite um número: ')))


for elemento in range(0, len(lista)):
    somaLista += lista[elemento]

print(f"A soma dos valores é {somaLista}")
""" 
SOLUÇÃO ADICIONAL DO CURSO
np.array(lista).sum()
"""

""" exercicio 2 """
notaAlunos = {}

for notas in range(0, 3):
    nome = input('Digite o nome do aluno: ')
    nota = float(input('Digite a nota: '))
    notaAlunos[nome] = nota

somaNotas = 0
print(notaAlunos)

for value in notaAlunos.values():
    somaNotas += value

media = somaNotas / len(notaAlunos)
print('A média das notas foi ', media)

""" exercicio 3 """
matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])

sumItems = 0
for i in range(0, matrix.shape[0]):
    for j in range(0, matrix.shape[1]):
        sumItems += matrix[i, j]

print(sumItems)    