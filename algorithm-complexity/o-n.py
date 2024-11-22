import timeit 

def soma(n):
    inicio = 0
    for i in range(n + 1):
        inicio = inicio + i
    return inicio


""" executada com 11 passos O(n) - proporcional ao valor de entrada"""
exec_time = timeit.timeit(lambda: soma(10), number=1000)
print(f"O algoritmo de soma rodou em {exec_time:.6f}")

""" executada em apenas 3 passos O(3)"""
def soma2(n):
    return n * (n + 1) / 2

exec_time2 = timeit.timeit(lambda: soma2(10), number=1000)
print(f"O algoritmo de soma2 rodou em {exec_time2:.6f}")


""" O(n) - O(1000)"""
def lista():
    list = []
    for i in range(1000):
        list.append(i)
    return list

exec_time_lista = timeit.timeit(lambda: lista(), number=1000)
print(f"{exec_time_lista:.6f}")


def lista2():
    return range(1000)

exec_time_lista2 = timeit.timeit(lambda: lista2(), number=1000)
print(f"{exec_time_lista2:.6f}")