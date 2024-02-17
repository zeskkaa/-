# задания 4
n = int(input())
str = []
for i in range(n):
    string = input()
    str.append(string)
letter_num = int(input())
for string in str:
    if len(string) >= letter_num:
        print(string[letter_num-1])


