# demo generator func
def generator_func(num):
    for i in range(num):
        yield i

num = 100
for item in generator_func(num):
    print (item)


# range VS list(range) is a good example of generator VS non-generator
# while range is a generator method, so don't really save data with extra memory,
# However, list will have to save everything in-memory which would 
# cost must memory resource and slow speed 