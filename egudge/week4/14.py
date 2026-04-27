from datetime import datetime,  timedelta,timezone
import math

def sign(a,b):
    if a=='-':
        return -b
    else:
        return +b
    

n=input().split()
x=input().split()
def difference(n,x):
    hours1=int(n[1][4:6])
    hours2=int(x[1][4:6])
    sign1=n[1][3:4]
    sign2=x[1][3:4]
    minutes1=int(n[1][7:9])
    minutes2=int(x[1][7:9])
    
    sign_hours1=sign(sign1,hours1)
    sign_hours2=sign(sign2,hours2)
    
    
    date1=n[0]
    date2=x[0]
    
    year1  = int(date1[0:4])
    month1 = int(date1[5:7])
    day1   = int(date1[8:10])
    year2  = int(date2[0:4])
    month2 = int(date2[5:7])
    day2   = int(date2[8:10])
    
    dt_1=datetime(year1, month1, day1, hours1, minutes1, 00)
    dt_2=datetime(year2, month2, day2, hours2, minutes2, 00)
    
    tz_1 = timezone(timedelta(hours=sign_hours1))
    tz_2 = timezone(timedelta(hours=sign_hours2))


    
    dt_aware_1 = dt_1.replace(tzinfo=tz_1)
    dt_aware_2 = dt_2.replace(tzinfo=tz_2)
    days=abs(dt_aware_1 - dt_aware_2)
    
    more_accurate=int(days.total_seconds())
    final=int(more_accurate//86400)
    return final

s=difference(n,x)
print(s)