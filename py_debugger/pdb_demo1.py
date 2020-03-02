"""
pdb -- A py built in debugger demo 
https://docs.python.org/3/library/pdb.html
"""
import pdb

def add(num1, num2):
    pdb.set_trace()
    return num1 + num2 

if __name__ == '__main__':
    """
    pdb useful command 
    
    help
    a 
    next
    list
    step
    """
    add(4, "abcvswfwe")