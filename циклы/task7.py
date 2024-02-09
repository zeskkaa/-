#задание 7
num = int(input())
max_num = -1
while num > 0:
    a = num % 10
    if a % 2 == 0 and a >max_num:
        max_num = a
    num = num // 10
if max_num == -1:
    print("нету такого числа")
else:
    print(max_num)
        