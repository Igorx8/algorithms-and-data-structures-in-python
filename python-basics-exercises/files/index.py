with open('./frase1.txt') as tex:
    for linha in tex:
        print(linha)


with open ('./frase1.txt') as tete:
    r = tete.readlines()
    print(r)
    

with open('./frase2.txt', 'w') as text2:
    text2.write('Olá mundo!')