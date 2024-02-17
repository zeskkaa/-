# задание 5
word = input().split()
lst = [[word[0]]]
for i in range(1, len(word)):
    if word[i] == word[i - 1]:
        lst[-1].append(word[i])
    else:
        lst.append([word[i]])
print(lst)