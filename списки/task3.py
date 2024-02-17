# задания 3
alf = "abcdefghijklmnopqrstuvwxyz"
lst = []
for i in range(len(alf)):
    element = alf[i] * (i+1)
    lst.append(element)
print(lst)