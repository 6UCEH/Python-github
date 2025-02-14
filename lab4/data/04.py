from datetime import datetime

date1 = datetime(2024, 1, 26, 0, 0, 0) #My birthday)
date2 = datetime(2024, 2, 14, 12, 0, 0)

difference_in_seconds = abs((date2 - date1).total_seconds())

print("Difference in seconds:", difference_in_seconds)
