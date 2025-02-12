from datetime import datetime

x = datetime.now()

y = x.replace(microsecond=0)

print("Current Datetime:", x)
print("Datetime without microseconds:", y)
