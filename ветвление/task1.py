#задание 1
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('равносторонний')
elif a == b or b == c or a == c:
    print('равнобедренный')
else:
    print('разносторонний')