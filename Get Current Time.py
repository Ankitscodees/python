from datetime import datetime

today_date = datetime.now()

time_now = today_date.strftime("%H:%M:%S")
print(f"The current time is {time_now}")
