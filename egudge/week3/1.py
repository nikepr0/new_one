
"""n = int(input())

valid = True
while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        valid = False
        break
    n //= 10

print("Valid" if valid else "Not valid")"""
"""Problem 301: 74803. Valid Number

Given an integer number , write a function for checking whether this number is valid. A valid number is one consisting of even digits only.
Input format

One integer — .
Output format

If the number is valid, print Valid; otherwise, print Not vali
    """

n=int(input())
chek = True
while n>0:
    last=n%10
    if last%2!=0:
        chek=False
        break
    n//=10

if chek:
    print("Valid")
else:
    print("Not Valid")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    