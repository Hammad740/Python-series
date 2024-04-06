
import datetime

mytime = datetime.time(12, 20, 1, 20)
print(mytime)
mytime_now = datetime.datetime.now()
print(mytime_now)

today = datetime.date.today()
print(today)
print(today.month)
print(today.year)
print(today.day)
print(today.ctime())
