# OS module - use to interact with the OS
# get working dir, change dir, check if file exists, get fileName, get size of file, env

import os

print(os.name)  # posix is the name when run this command in MAC/UNIX
print(os.getcwd()) # to knw your current working dir
print(os.listdir("/Users/datashan/Desktop/Test Automation/Py3xLearning/Ex_05072024")) # this will list all the folders
# files present in the directory path given above
# os.mkdir("folder name") # this will create a folder/dir within the current directory

# to list all the directories at once

all_files = os.listdir("/Users/datashan/Desktop/Test Automation/Py3xLearning/Ex_05072024")
print(all_files)

# environment variables
# like JAVA_HOME, PATH, CLASSPATH, etc
print(os.environ)

# set a new one
os.environ['MY_VAR'] = 'pramod'
print(os.environ['MY_VAR'])

# walk in to directories
# check how many dir, files are there in a path

for root, dirs, files in os.walk("/Users/datashan/Desktop/Test Automation/Py3xLearning/Ex_05072024"):
    print(root)
    print(dirs)
    print(files)


# How to open, write and close a file
# open a file
file = os.open("sample.txt", os.O_RDWR)
os.write(file, b"Hello, World!")
os.close(file)