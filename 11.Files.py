# Reading the Text FIle
import os
f=open("package.py" , "r")
f.seek(50)
print(f.read())
# Writing data into file
f=open("test.txt" , "w")
f.write("Hello world")
# File Permissions
print("Test file has read permission: ", os.access("test.txt", os.R_OK))
print("Test file has write permission: ",os.access("test.txt", os.W_OK))
print("Test file has execute permission: ",os.access("test.txt", os.X_OK))
