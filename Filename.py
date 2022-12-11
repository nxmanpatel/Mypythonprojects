import os
filename= input(print("Enter a filename-"))
# unpacking the tuple
file_name, file_extension = os.path.splitext("abc.py")
print(file_extension)


