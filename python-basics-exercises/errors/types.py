""" Erro de variável não definida. (NameError) """
print('Meu nome é ', nome)

""" Erro de divisão por zero. (ZeroDivisionError) """
print(10/0)

""" Tipos de dados incompatíveis em operação. (TypeError) """
print(2.3/'string')

""" Erro de índice inexistente. (IndexError) """
lista = [1, 2, 3]

""" Erro de valor inconsistente. (ValueError) """
try:
    valor = int(input('Digite um número')) # Se digitar uma string, ocorre ValueError
except:
    print('Valor inválido')
else:
    print(f"O valor digitado é {valor}")


while True:
    try:
        numero = int(input('Digite um número: '))
    except ValueError:
        print('Valor inválido')
    except KeyboardInterrupt:
        print('Usuário interrompeu a execução')
        break
    else:
        print(f"O valor digitado é {numero}")
        break