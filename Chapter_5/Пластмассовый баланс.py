def largest_power(n, k):
    count = 0
    power = k
    while power <= n:
        count += n // power
        power *= k
    return count
n = 10  
k = 2   
result = largest_power(n, k)
print(f"Наибольшая степень x, такая что {n} делится на {k}^x: {result}")
