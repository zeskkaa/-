# задания 7
n = int(input())
lst = []
for _ in range(n):
    line = input()
    lst.append(line)
search_str = input()
found_strings = [s for s in lst if search_str in s]
if found_strings:
    print()
    for s in found_strings:
        print(s)
else:
    print()
