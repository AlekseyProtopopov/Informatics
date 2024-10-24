bin_13 = bin(13)[2:]
bin_45 = bin(45)[2:]
bin_100 = bin(100)[2:]
sum_1 = bin(int('1011', 2) + int('1101', 2))[2:]
sum_2 = bin(int('101010', 2) + int('110110', 2))[2:]
diff_1 = bin(int('101010', 2) - int('11001', 2))[2:] 
diff_2 = bin(int('110010', 2) - int('10110', 2))[2:]
mul_1 = bin(int('101', 2) * int('110', 2))[2:]
mul_2 = bin(int('1011', 2) * int('1101', 2))[2:] 
div_1 = bin(int('101010', 2) // int('101', 2))[2:]
div_2 = bin(int('110110', 2) // int('100', 2))[2:]
print(bin_13)
print(bin_45)
print(bin_100)
print(sum_1)
print(sum_2)
print(diff_1)
print(diff_2)
print(mul_1)
print(mul_2)
print(div_1)
print(div_2)