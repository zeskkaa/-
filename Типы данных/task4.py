# задание 4
num = int(input())
if num < 0:
    num *= (-1)
a = (num // 100)
b = (num % 100 // 10)
c = (num % 10)
print(a * 100 + b * 10 + c)
print(a * 100 + c * 10 + b)
print(b * 100 + a * 10 + c)
print(b * 100 + c * 10 + a)
print(c * 100 + a * 10 + b)
print(c * 100 + b * 10 + a)