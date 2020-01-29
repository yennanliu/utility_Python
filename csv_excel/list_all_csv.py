# python 3 
import os
def main():
    csv_list = os.listdir("your_directory")
    print (csv_list)
    return csv_list

if __name__ == '__main__':
    main()