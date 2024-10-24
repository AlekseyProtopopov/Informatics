def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return abs(x)  

def binary_gcd(x, y):
    if x == 0 and y == 0:
        return 0  

    greatest_common_divisor = gcd(x, y)  
    return bin(greatest_common_divisor).count('1')
print(binary_gcd(666666, 333111))  
print(binary_gcd(545034, 5))  
print(binary_gcd(0, 0))  
print(binary_gcd(0, 76899299))  
print(binary_gcd(-124, -16))  
