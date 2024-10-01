from datetime import datetime


current_datetime = datetime.now()


datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Current DateTime with Microseconds:", current_datetime)
print("DateTime without Microseconds:", datetime_without_microseconds)
