import datetime
from datetime import datetime, timedelta

x = datetime.datetime.now()
print(x)

# --- creating date object

x = datetime.datetime(2020, 5, 17)
print(x)

# --- The strftime() Method

dt = datetime(2024, 6, 15, 14, 30, 59)

dt.strftime("%Y-%m-%d")       # '2024-06-15'
dt.strftime("%d.%m.%Y")       # '15.06.2024'
dt.strftime("%H:%M:%S")       # '14:30:59'
dt.strftime("%d %B %Y, %A")   # '15 June 2024, Saturday'

# ---

dt1 = datetime(2024, 1, 1)
dt2 = datetime(2024, 6, 15)

delta = dt2 - dt1
print(delta)           # 166 days, 0:00:00
print(delta.days)      # 166
print(delta.seconds)   # 0
print(delta.total_seconds())  # 14342400.0