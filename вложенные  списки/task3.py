# задание 3
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total_sum = sum(sum(i) for i in list1)
total_count = sum(len(i) for i in list1)
result = total_sum / total_count
print(result)
