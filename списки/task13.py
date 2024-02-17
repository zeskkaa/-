# задания 13
num = input()
numbers = list(map(int, num.split()))
result = [num1**2 for num1 in numbers if num1 % 2 == 0 and num1 % 10 != 4]
print(result)
