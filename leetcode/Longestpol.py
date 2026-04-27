class Solution:
    def __init__(self, s:str , le:int ):
        self.s=s
        self.lenght=le
    def longestPalindrome(self, s: str ,l:int , max_m=0) -> str:
        for i in range(l):
            for j in range(-1 ,-l ,-1):
                if s[i]==s[j] & :
                    i2=i; j2=j
                    m=+1; pos=[i,j]
                else:
                    continue
                if m>max_m:
                    max_m=m
s=input()
leng=len(s)
print(d.longestPalindrome(s,leng))