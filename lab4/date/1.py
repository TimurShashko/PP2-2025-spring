import datetime

x = datetime.datetime.now()
y = x - datetime.datetime(1, 1, 6) + datetime.datetime(1, 1, 1)
print(y)

#second way
print("")
from datetime import timedelta
fivedago = x - timedelta(days = 5)
print("5 days ago was:", fivedago.strftime("%Y-%m-%d"))