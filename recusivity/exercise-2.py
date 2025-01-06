def recursive2(a, b):
    if b == 0:
        return 1
    
    return a * recursive2(a, b - 1)

print(recursive2(2, 2))

