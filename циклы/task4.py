# задание 4
n = int(input())
s = sum(range(1, n+1))
for _ in range(n-1):
   s -= int(input())
print(s)