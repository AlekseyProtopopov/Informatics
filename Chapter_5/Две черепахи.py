def race(v1, v2, g):
    if v1 >= v2:
        return [-1, -1, -1]
    
    time_in_hours = g / (v2 - v1)
    
    hours = int(time_in_hours)
    minutes = int((time_in_hours - hours) * 60)
    seconds = round(((time_in_hours - hours) * 60 - minutes) * 60)
    
    return [hours, minutes, seconds]

result = race(720, 850, 70)
print(result)
