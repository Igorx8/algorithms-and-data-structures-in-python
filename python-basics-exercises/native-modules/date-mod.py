import datetime

print(dir(datetime))
print('\n')
print(datetime.date.today())
print(datetime.datetime.now())

data = datetime.date(2020, 7, 10)
print(data)
print(data.day)
print(data.month)
print(data.year)


horario = datetime.datetime(2020, 7, 10, 7, 30, 0)
print(horario)
print(horario.hour)
print(horario.minute)
print(horario.second)