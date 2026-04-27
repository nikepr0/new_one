a=int(input())
n=list(map(int,input().split()))
print("Yes" if all(n[p]>=0 for p in range(len(n))) else "No")