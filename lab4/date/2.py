import datetime
from datetime import timedelta
x = datetime.datetime.now()
delta = timedelta(days = 1)
print("yesterday:", (x - delta).strftime("%Y-%m-%d"), "today:", x.strftime("%Y-%m-%d"), "tomorrow:", (x + delta).strftime("%Y-%m-%d"))