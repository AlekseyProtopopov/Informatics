def f(num):
    num_str = str(num)
    parts = []
    for i, digit in enumerate(num_str):
        if digit != '0':  
            parts.append(digit + '0' * (len(num_str) - i - 1))
    return ' + '.join(parts)
print(f(12))     
print(f(42))     
print(f(70304))  
