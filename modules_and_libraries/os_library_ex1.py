# os module 
# accessing files, folder and system related stuff

import os
from datetime import datetime

print("CURRENT WORKING DIRECTORY:",os.getcwd())

content = os.listdir()
print("Content of current folder",content)

content = os.listdir("C:/Program Files")
print("Content of Program files folder")
print(content)

# check if folder exists
if os.path.exists("files"):
    print("folder exists")
    # check if a file exists
    if os.path.exists("files/great gatsby.txt"):
        print("file found")
    else:
        print("file not found")
else:
    print("folder does not exist")

# get details of a file
file= "files/great gatsby.txt"
size = os.path.getsize(file)
print("Size of file is:",size//1024, "KB")
createdOn = os.path.getctime(file)
print("Created on:",datetime.fromtimestamp(createdOn))

# 
