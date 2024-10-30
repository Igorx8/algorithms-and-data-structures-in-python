idade = int(input('Digite sua idade: '))
if(idade < 0):
    print('Idade inválida')
else:
    if(idade >= 0 and idade <= 12):
        print('Você é uma criança')
    else:
        if(idade >= 13 and idade <= 17):
            print('Você é um adolescente')
        else:
            print('Você é um adulto')