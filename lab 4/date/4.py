from datetime import datetime


date1 = datetime(2024, 10, 1, 10, 0, 0)  
date2 = datetime(2024, 10, 1, 12, 30, 0)  

difference_in_seconds = abs((date2 - date1).total_seconds())

print(f"Difference between the two dates in seconds: {difference_in_seconds} seconds")
