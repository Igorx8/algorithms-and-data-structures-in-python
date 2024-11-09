alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open('./exercise-6-response.txt', 'w') as exResponse:
    for name, nota in alunos.items():
        exResponse.write(f"{name}, {nota} \n")