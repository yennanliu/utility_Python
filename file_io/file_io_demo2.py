"""
file IO with error handling 
"""
try:
    with open("fileIO/my_dummy_file.txt", mode='r') as f:
        print (f.read())
except FileNotFoundError as err:
    print ("file dons not exist")
    raise err
except IOError as err:
    print ("IO error")
    raise err