# задание 10
num = input().split()
lst = []
for i in num:
    lst.append(int(i))
num_max = max(lst)
num_min = min(lst)
num_max_index = lst.index(num_max)
num_min_index = lst.index(num_min)
lst[num_max_index], lst[num_min_index]  = lst[num_min_index],lst[num_max_index] 
print (*lst)