# https://docs.python.org/3/library/multiprocessing.html

from multiprocessing import Pool

def f(x):
    print (x)
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))