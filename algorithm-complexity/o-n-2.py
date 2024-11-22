""" O(n²) """
def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)

print(quadratic([0, 1, 2]))

def combination(n):
    """ O(1) """
    print(n[0])

    """ O(5) """
    for i in range(5):
        print('test', i)

    """ O(n) """
    for i in n:
        print(i)

    """ O(n) """
    for i in n:
        print(i)
    
    """ O(3) """
    print('Python')
    print('Python')
    print('Python')

""" O(1) + O(5) + O(n) + O(n) + O(3) = O(9) + O(2n) -> O(n)"""
print(combination([5]))