m1 = float(input('Digite a nova da primeira prova: '))
m2 = float(input('Digite a nova da segunda prova: '))
m3 = float(input('Digite a nova da terceira prova: '))

media = (m1 + m2 + m3) / 3

print(media)

if(media >= 0 and media <= 4):
    print('O aluno está reprovado')
else:
    if(media > 4 and media <= 6):
        print('Aluno pegou exame')
        notaExame = float(input('Digite a nota do exame: '))
        if(notaExame >= 6):
            print('Aluno aprovado')
        else:
            print('Aluno reprovado')
    else:
        print('Aluno aprovado')