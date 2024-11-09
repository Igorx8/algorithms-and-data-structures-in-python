lista = []

while True:
    try:
        lista.append(float(input('Digite um número: ')))
        lista.append(float(input('Digite outro número: ')))
        division = lista[0] / lista[1]
    except ZeroDivisionError:
        print('Divisão por zero não habilitada')
    except ValueError:
        print('Valor inválido')
    except KeyboardInterrupt:
        print('\n O usuário interrompeu a execução')
        break
    else:
        print(f"A divisão é {division}")
        break


