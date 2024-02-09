# задание 2
counter = 0
num = int(input())
while num != 0:
    counter += int(num % 10 == 0)
    num//= 10
print(counter)

