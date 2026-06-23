import os
from pathlib import Path
import shutil

# File and path operations: os, shutil, pathlib
# Directory management: os.mkdir(),
# os.makedirs(), os.listdir(), os.chdir(), os.getcwd(), os.rmdir()

print(os.getcwd()) # where are we RIGHT NOW
os.chdir("any_folder") # аналог cd
print(os.listdir()) # list of files
os.mkdir("test_folder") # create 1 folder
os.makedirs("a/b/c") # create folder chain
os.rmdir("test_folder") # deletes empty folder, works only if the folder is empty

# ----------------------------------------------

shutil.copy("file.txt", "copy.txt") # copy the file
shutil.rmtree("folder") # remove tree (deletes folder even it is not emtpy)
shutil.move("file.txt", "folder/file.txt") # moving file / folder

# ----------------------------------------------

print(Path.cwd())                          # where we are now
print(list(Path(".").iterdir()))           # list of files
Path("test_folder").mkdir()                # create folder
Path("a/b/c").mkdir(parents=True)          # create a chain of folders
Path("test_folder").rmdir()                # remove empty folder