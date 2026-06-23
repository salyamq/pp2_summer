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

def data_diff(d1, d2):
    date1 = datetime.datetime(*d1)
    date2 = datetime.datetime(*d2)
    diff = date2 - date1
    return diff.total_seconds()

list1 = input().split(",")
list2 = input().split(",")
data1 = [int(i) for i in list1]
data2 = [int(i) for i in list2]

print(data_diff(data1, data2))








