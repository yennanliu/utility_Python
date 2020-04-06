import heapq
import sys
 
def merge_file():
    # https://rosettacode.org/wiki/Stream_Merge#Python
    #sources = sys.argv[1:]
    sources = ["eggs.txt", "spam.txt"]
    for item in heapq.merge(open(source) for source in sources):
        #for data in item:
        print(item.readline())

def merge_array():
    # http://blog.moertel.com/posts/2013-05-26-python-lazy-merge.html
    xs = heapq.merge(range(3), range(2, 9), range(5))
    return list(xs)

if __name__ == '__main__':
    merge_file()