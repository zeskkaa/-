# задание 4
n = int(input())
list1 = [[i+1 for i in range(n)] for _ in range(n)]
list2 = [i for i in list1 if len(i) == n]
for i in list2:
    print(i)
