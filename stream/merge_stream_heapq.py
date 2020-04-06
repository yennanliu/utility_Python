import heapq
import sys
import itertools
 
def merge_file():
    # https://rosettacode.org/wiki/Stream_Merge#Python
    # https://github.com/python/cpython/blob/2.7/Lib/heapq.py
    #sources = sys.argv[1:]
    sources = ["eggs.txt", "spam.txt"]
    for item in heapq.merge(open(source) for source in sources):
        #for data in item:
        print(item.readline())

def merge_array_heapq():
    # http://blog.moertel.com/posts/2013-05-26-python-lazy-merge.html
    xs = heapq.merge(range(3), range(2, 9), range(5))
    return list(xs)

def merge_array_sorted():
    #https://docs.python.org/2/library/heapq.html
    """
    In [77]: itertools.chain('ABC', 'DEF')
    In [78]: list(itertools.chain('ABC', 'DEF'))
    Out[78]: ['A', 'B', 'C', 'D', 'E', 'F']
    """
    xs = sorted(itertools.chain(range(3), range(2, 9), range(5))) 
    return list(xs)

if __name__ == '__main__':
    merge_file()