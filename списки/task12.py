# задание 12
num = input()
num1 = list(map(int, num.split()))
sorted_num_asc = sorted(num1)
sorted_num_desc = sorted(num1, reverse=True)
print(sorted_num_asc)
print(sorted_num_desc)
