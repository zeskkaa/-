#задание 6
from math import sqrt


a, b, c = float(input()), float(input()), float(input())
d = (b**2) - (4*a*c)
if d > 0:
    x1 = (-b - sqrt(d)) / (2*a)
    x2 = (-b + sqrt(d)) / (2*a)
    print(min(x1, x2))
    print(max(x1, x2))
elif d == 0:
    print(-b / (2*a))
else:
    print("Нет корней")

