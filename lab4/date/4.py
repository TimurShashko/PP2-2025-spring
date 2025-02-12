from datetime import datetime

date1 = datetime(2025, 2, 5, 14, 30, 0)
date2 = datetime(2025, 2, 3, 12, 15, 0)

difference = (date1 - date2).total_seconds()

print("Difference in seconds:", difference, "seconds")
