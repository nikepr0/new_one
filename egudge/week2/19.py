n = int(input())
dic = {}

for i in range(n):
    s = input()
    lst = list(map(str, s.split()))
    dorama = lst[0]
    number = int(lst[1])
    if dorama not in dic:
        dic[dorama] = number
    else:
        dic[dorama] += number

num = dict(sorted(dic.items()))

for i in num:
    print(i, num[i])