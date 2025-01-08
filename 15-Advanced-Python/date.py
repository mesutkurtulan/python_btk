import datetime
from datetime import datetime
from datetime import timedelta
result = dir(datetime)

print(result)   # ['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']

result = datetime.now()
print(result)   # 2025-01-08 22:58:44.464425

result = datetime.now().date()
print(result)   # 2025-01-08

result = datetime.now().time()
print(result)   # 22:59:38.174450

result = datetime.now().year
print(result)   # 2025

result = datetime.now().month
print(result)   # 1

result = datetime.now().day
print(result)   # 8

result = datetime.now().hour
print(result)   # 23

result = datetime.now().minute
print(result)   # 1

result = datetime.today()
print(result)   # 2025-01-08 23:02:15.322904

result = datetime.ctime(datetime.now())
print(result)   # Wed Jan  8 23:03:38 2025

result = datetime.strftime(datetime.now(),'%Y')
print(result)   # 2025

result = datetime.strftime(datetime.now(),'%d')
print(result)   # 08

result = datetime.strftime(datetime.now(),'%A')
print(result)   # Wednesday

result = datetime.strftime(datetime.now(),'%B')
print(result)   # January

result = datetime.strftime(datetime.now(),'%X')
print(result)   # 23:05:22

result = datetime.strftime(datetime.now(),'%Y %B %d %A')
print(result)   # 2025 January 08 Wednesday

t = '21 April 2019'

day, month, year = t.split()
print(day, month, year) # 21 April 2019

t = '21 April 2019 hour 10:12:30'

dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
print(dt)   # 2019-04-21 10:12:30

birthday = datetime(1983,5,9)
print(birthday)     # 1983-05-09 00:00:00
print(datetime.timestamp(birthday))     # 421275600.0 Timestamp

print(datetime.fromtimestamp(datetime.timestamp(birthday))) # 1983-05-09 00:00:00

print(datetime.fromtimestamp(0))    # 1970-01-01 02:00:00

print(datetime.now() - birthday)    # 15220 days, 23:19:07.187095   #deltatime

print(datetime.now() + timedelta(days=10)) # 2025-01-18 23:22:07.914136
