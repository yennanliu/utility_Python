# https://stackoverflow.com/questions/4617034/how-can-i-open-multiple-files-using-with-open-in-python

with open('stream/spam.txt', 'r') as a, \
     open('stream/eggs.txt', 'r') as b:

     for line in zip(a.readlines(), b.readlines()):
        print (line)