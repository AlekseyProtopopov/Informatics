def find_lowest_int(k1):
    k2 = k1 + 1
    n = 1
    while True:
        product_k1 = n * k1
        product_k2 = n * k2
        
        if sorted(str(product_k1)) == sorted(str(product_k2)):
            return n
        
        n += 1
print(find_lowest_int(100))  
print(find_lowest_int(325))   
