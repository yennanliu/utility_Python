# https://docs.python.org/3/library/fileinput.html

import fileinput
from fileinput import FileInput

with FileInput(files=('stream/spam.txt', 'stream/eggs.txt')) as input:
    for line in input:
        print (line)