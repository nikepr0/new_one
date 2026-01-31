a=input()
b=0
for i in a:
    if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
        b+=1
if b==len(a):
    print("int")
else:
    print("str")