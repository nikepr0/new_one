n = int(input())
lst = list(map(int, input().split()))

ind = 0
for i in lst:
    if i in lst[0:ind]:
        print("NO")
    else:
        print("YES")
    ind += 1