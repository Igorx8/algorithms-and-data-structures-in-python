""" exercicio 1 """
def read_temperature():
    c = float(input('Digite a temperatura e Cº: '))
    return c

def convertToFahrenheit(temperaturaEmCelsius):
    fahrenheit = (9 * temperaturaEmCelsius + 160) / 5
    return fahrenheit

def mostrar(temperaturaF):
    print(f"A temperatura em fahrenheit é {temperaturaF}")

c = read_temperature()
cToF = convertToFahrenheit(c)
mostrar(cToF)

""" exercicio 2 """
def calcDistancia(tempoGasto, velMedia):
    distancia = tempoGasto * velMedia
    return distancia

def calcLitrosUsados(distancia):
    litrosUsados = distancia / 12
    return litrosUsados

def lerValores():
    velMedia = float(input('Qual a velocidade média durante a viagem: '))
    tempoGasto = float(input('Qual o tempo gasto durante a viagem: '))
    return { 'velMedia': velMedia, 'tempoGasto': tempoGasto }

def mostraResult(valores):
    distancia = calcDistancia(valores["tempoGasto"], valores["velMedia"])
    litrosUsados = calcLitrosUsados(distancia)
    print(f'A distância foi de {distancia}km e foram usados {litrosUsados} litros')

valores = lerValores()
mostraResult(valores)
