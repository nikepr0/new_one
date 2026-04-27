arr=input().strip("[]")
a=arr.split(",")
arr=[int(i) for i in a]
tar=int(input())

def ts(a , t):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i]+a[j]==t:
                return [i, j]

print(ts(arr, tar))