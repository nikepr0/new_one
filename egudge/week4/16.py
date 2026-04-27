from datetime import datetime 
line1 = input().strip()
line2 = input().strip()


date_time_part1, utc_part1 = line1.rsplit(" UTC", 1)
date_time_part2, utc_part2 = line2.rsplit(" UTC", 1)
utstime1=line1[-6:]
utstime2=line2[-6:]

dt1 = datetime.strptime(date_time_part1, "%Y-%m-%d %H:%M:%S")
dt2 = datetime.strptime(date_time_part2, "%Y-%m-%d %H:%M:%S")

print(int(abs((dt2-dt1).total_seconds()+int(utstime2[1:3])*3600-int(utstime1[1:3])*3600+int(utstime2[4:6])*60-int(utstime1[4:6])*60)))