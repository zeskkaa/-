# задание 6
fib1 = fib2 = 1
num = int(input())
print(fib1, fib2, end=' ')
for i in range(2, num):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
