# Create a text file and write sample data
# Read and print file contents
# Append new lines and verify content
# Copy and back up files using shutil
# Delete files safely
import shutil
import os

with open("data.txt", "w") as file:
    file.write("Helloooo\n")
    file.write("Good byee\n")

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

with open("data.txt", "a") as file:
    file.write("new line1\n")
    file.write("new line2\n")
with open("data.txt", "r") as file:
    print(file.read())

shutil.copy("data.txt", "backup_data.txt")

if os.path.exists("backup_data.txt"):
    os.remove("backup_data.txt")
