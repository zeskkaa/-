# задание 5 
max1 = float('-inf')
max2 = float('-inf')
max3 = float('-inf')
while True:
    num = input("Введите число: ") 
    if num.lower() == "стоп":
        break       
    num = float(num)
    if num > max1:
        max3 = max2
        max2 = max1
        max1 = num
    elif num > max2:
        max3 = max2
        max2 = num
    elif num > max3:
        max3 = num
print(max1, max2, max3)