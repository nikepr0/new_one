n=input()
vowel=["a","e","i","o","u","A","E","I","O","U"]
print("Yes" if any(n[p] in vowel for p in range(len(n))) else "No")