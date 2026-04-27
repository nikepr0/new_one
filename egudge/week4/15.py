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
    
    birthday=datetime(year1,month1,day1,0,0,0)
    current=datetime(year2,month2,day2,0,0,0)
    
    tz_nyc_1 = timezone(timedelta(hours=sign_hours1, minutes=minutes1))
    tz_nyc_2 = timezone(timedelta(hours=sign_hours2, minutes=minutes2))
    
    birth=birthday.replace(tzinfo=tz_nyc_1)
    curre_aware=current.replace(tzinfo=tz_nyc_2)
    
    candidate_this_year=datetime(year2,month1,day1,0,0,0)
    tz=timezone(timedelta(hours=sign_hours2, minutes=minutes2))
    
    candidate_this_year = datetime(year2, month1, day1, 0,0,0)
    test = candidate_this_year.replace(tzinfo=tz)   

    if test >= curre_aware:               
        target = test
        delta = target - curre_aware
        if delta.total_seconds() < 0:           
            next_y = year2 + 1
            candidate_next = datetime(next_y, month1, day1, 0,0,0)
            target = candidate_next.replace(tzinfo=tz)
            delta = target - curre_aware
    else:
        next_y = year2 + 1
        candidate_next = datetime(next_y, month1, day1, 0,0,0)
        target = candidate_next.replace(tzinfo=tz)

    
    
    return delta.days
s=difference(n,x)
print(s)
