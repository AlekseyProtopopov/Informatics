
def tetration(x, n):
    if n == 0:
        return 1  
    return x ** tetration(x, n - 1)  

result_3_5 = tetration(3, 5)
result_5_2 = tetration(5, 2)

print(result_3_5)
print(result_5_2)

print(len(str(result_3_5)))
print(len(str(result_5_2)))
