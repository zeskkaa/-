# задания 8
num = input()
num_list = num.split()
count_greater_than_50 = 0
for i in num_list:
    if i.isdigit() and int(i) > 50:
        count_greater_than_50 += 1
print(count_greater_than_50)
