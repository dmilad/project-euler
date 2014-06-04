import datetime


d1 = datetime.date(1901, 1, 1)
d2 = datetime.date(2000, 12, 31)

count = 0
while d1 < d2:
    if d1.weekday() == 6 and d1.day == 1:
        count += 1 
    d1 += datetime.timedelta(days = 1)

print count