def plastic_balance(lst):
    while len(lst) > 2: 
        left_sum = lst[0] + lst[-1]  
        middle_sum = sum(lst[1:-1])  

        if left_sum == middle_sum:  
            return lst[1:-1]

        lst = lst[1:-1]  

    return []

print(plastic_balance([1,2,3,4,5]))  
print(plastic_balance([0,104,3,101,0,111])) 
print(plastic_balance([1,-1])) 
print(plastic_balance([0]))  
print(plastic_balance([100,0,-100]))  
print(plastic_balance([4,4])) 
