"""
file IO with error handling 
"""

def main(file_name):
    try:
        with open(file_name, mode='r') as f:
            print (f.read())

    except FileNotFoundError as err:

        print ("file dons not exist")
        raise err

    except IOError as err:
        print ("IO error")
        raise err

if __name__ == '__main__':
    file_name = "fileIO/my_dummy_file.txt"
    main(file_name)