#задание 2
num1 = int(input())
num2 = int(input())
operator = input()
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)    
elif operator == "/":
    if num2 == 0:
        print('на ноль делить нельзя!')
    else:
        print(num1 / num2)
elif operator == '//':
    if num2 == 0:
        print('на ноль делить нельзя!')
    else:
        print(num1 // num2)
elif operator == "**":
    print(num1 ** num2)
        
    