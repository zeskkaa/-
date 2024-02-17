# задание 6
n = int(input())
lst = []
for _ in range(n):
    line = input()
    if line not in lst:
        lst.append(line)
for s in lst:
    print(s)
