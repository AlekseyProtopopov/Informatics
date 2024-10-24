str1 = input().strip()
str2 = input().strip()

if str1.lower() < str2.lower():
    print("-1")
elif str1.lower() > str2.lower():
    print("1")
else:
    print("0")
