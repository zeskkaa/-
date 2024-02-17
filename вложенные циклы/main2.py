# задание 2
num = int(input())
c = 1
sum = 0
for i in range(1, num + 1):
    c *= i
    sum += c
print(sum)
