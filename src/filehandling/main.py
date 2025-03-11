# What is file handling?
# File handling is an important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files.
# file mode
# w -> write
# r -> read
# a -> append
# what is file
# A file is a named location on disk to store related information.
#  types of files
# 1. Text file
# 2. Binary file
# handle = open("filehandling/record.txt", "w")
# handle.write("Hi")
# handle.close()

# handle = open("filehandling/record.txt", "a")
# name =input("Enter your name: ")
# handle.write(f"Hi {name} \n")
# handle.close()


handle = open("filehandling/record.txt", "r")
# print(handle.read())
# print(handle.readline())
print(handle.readlines())

