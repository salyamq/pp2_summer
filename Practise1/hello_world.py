import re

text = """
[INFO] 2024-01-10 User login success
[ERROR] 2023-12-05 Disk full
[WARN] 2022-11-01 Low memory
[INFO] 2024-02-18 File uploaded
"""

date = re.findall(r"\d{4}-\d{2}-\d{2}", text)
level = re.findall(r"INFO|ERROR|WARN", text)
liss = []
for x, y in zip(date, level):
    liss.append((x, y))

print(liss)