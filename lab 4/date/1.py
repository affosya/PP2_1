from datetime import datetime, timedelta

current_date = datetime.now()


date_five_days_ago = current_date - timedelta(days=5)


print("Current Date:", current_date.strftime('%Y-%m-%d'))
print("Date 5 Days Ago:", date_five_days_ago.strftime('%Y-%m-%d'))
