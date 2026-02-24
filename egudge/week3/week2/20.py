n = int(input())
lst = []

for i in range(n):
    s = input()
    lst.append(s)

dic = {}

for i in lst:
    com = list(map(str, i.split()))
    if len(com) == 3:
        dic[com[1]] = com[2]
    elif len(com) == 2:
        if com[1] in dic:
            print(dic[com[1]])
        else:
            print(f"KE: no key {com[1]} found in the document")