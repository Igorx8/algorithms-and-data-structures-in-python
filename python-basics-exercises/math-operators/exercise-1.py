num1 = 2
num2 = 5

sumVar = num1 + num2
subtraction = num1 - num2 
mult = num1 * num2
div = num1 / num2

print(sumVar,  'result of sum')
print(subtraction, 'result of subtraction')
print(mult, 'result of multiplication')
print(div, 'result of division')

tempo = float(input('Digite o tempo gasto na viagem: '))
velocidadeMedia = float(input('Digite a velocidade média: '))

distancia = tempo * velocidadeMedia
litros_usados = distancia / 12

print('Distancia: ', distancia, '\nLitros usados: ', litros_usados)