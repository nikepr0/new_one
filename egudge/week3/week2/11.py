a, b, c = map(int, input().split())
list1=list(map(int,input().split()))
list1[b-1:c] = reversed(list1[b-1:c])
print(*list1)