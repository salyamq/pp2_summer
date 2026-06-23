# Create nested directories
# List files and folders
# Find files by extension
# Move/copy files between directories
import os
import shutil

os.makedirs("/data/files/files1", exist_ok=True)

items = os.listdir("data")
print(items)

folder = "data/files/files1"
for file in os.listdir(folder):
    if file.endswith(".txt"):
        print(file)

shutil.copy("data.txt", "data/files/files1/data.txt")
shutil.move("data.txt", "project/data/files/data.txt")


