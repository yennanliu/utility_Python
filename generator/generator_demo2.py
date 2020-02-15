# demo generator func
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print (iterator)
            print (next(iterator)) # not only print the (next(iterator)) , but also do the "next" generator command
        except StopIteration:
            break

special_for([1,2,3])