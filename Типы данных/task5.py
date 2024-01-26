#задание 5
num = int(input())
num1 = num % 10
num2 = num % 100 // 10
num3 = num // 100 % 10
num4 = num // 1000
print(num4, num3, num2, num1,sep = "\n")