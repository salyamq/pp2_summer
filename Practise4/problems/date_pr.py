import datetime

# ---
current = datetime.datetime.now()
print(current - datetime.timedelta(days=5))

# ---
print(current - datetime.timedelta(days=1))
print(current)
print(current + datetime.timedelta(days=1))

# ---

no_microseconds = current.replace(microsecond=0)
print(no_microseconds)

# ---

date1 = datetime.datetime(2026, 6, 16, 12, 0, 0)
date2 = datetime.datetime(2026, 6, 16, 12, 55, 59)
diff = date2 - date1
seconds = diff.total_seconds()

print(seconds)

