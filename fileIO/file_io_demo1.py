"""
file IO with different mode

https://stackoverflow.com/questions/16208206/confused-by-python-file-mode-w
https://www.tutorialspoint.com/python/python_files_io.htm

r : Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.

rb : Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.
 
r+ : Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
 
rb+ : Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.
 
w :Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

wb : Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

w+ : Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

wb+ : Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

a : Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

ab : Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

a+ : Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

ab+ : Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

"""

# mode = 'r' 
# Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
print ("="*30)
print ("model = r")
with open("fileIO/test.txt", mode='r') as f:
    print (f.read())

# mode = 'rb'
# Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.
print ("="*30)
print ("model = rb")
with open("fileIO/test.txt", mode='rb') as f:
    print (f.read())


# mode = 'r+'
# Opens a file for both reading and writing. The file pointer will be at the beginning of the file.
print ("="*30)
print ("model = r+")
with open("fileIO/test.txt", mode='r+') as f:
    print (f.read())

# mode = 'w'
# Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
print ("="*30)
print ("model = w")
with open("fileIO/test2.txt", mode='w') as f:
    print ("write to file with w mode")
    f.write("this is test2.txt with w mode")
    f.close()

# mode = 'wb'
# Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
print ("="*30)
print ("model = wb")
with open("fileIO/test2.txt", mode='wb') as f:
    print ("write to file with wb mode")
    f.write(b'this is test2.txt with wb mode')
    f.close()

# mode = 'w+'
# Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
print ("="*30)
print ("model = w+")
with open("fileIO/test2.txt", mode='w+') as f:
    print ("write to file with wb mode")
    f.write("this is test2.txt with w+ mode")
    f.close()
