# File modes: r, w, a, x

file_read = open("raw.txt", "r") # read, no file -> error
file_write = open("raw.txt", "w") # write, if the file exists, deletes the old version
file_append = open("raw.txt", "a") # append, adds text to the end of the file
file_create = open("raw.txt", "x") # create, if file exists -> error

# Reading files: read(), readline(), readlines()
file = open("raw.txt", "r")
text_read = file.read() # read all file
text_readline = file.readline() # reads one row
text_readlines = file.readlines() # # reads all the lines and creates list

# Writing and appending files
file = open("raw.txt", "w") # or "a" - append
file.write("Hello") # writing hello

lines = ["Hello\n", "World\n", "Python\n"] # writelines do not add \n automatically
file.writelines(lines)

# Context manager: with statement

with open("raw.txt", "r") as f: # opens the file
    data = f.read() # works with it
    # and closes it on its own



