n = int(input())
lst = list(map(int, input().split()))
cnt = {}

for i in lst:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
print(cnt.items())

for i in cnt:
    best_val = i
    best_freq = cnt[i]
    break

for i in cnt:
    if best_freq < cnt[i]:
        best_freq = cnt[i]
        best_val = i
    elif best_freq == cnt[i] and i < best_val:
        best_val = i

  
print(best_val)