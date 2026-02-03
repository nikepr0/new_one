a=int(input())
print("YES" if(a==pow(2,int(a.bit_length()-1))) else "NO")