# multiplu_by_2 is a fp function
# since it's a pure function 
# 1) always output same (with same input)
# 2) no side effect
def multiplu_by_2(my_input):
    r = []
    for item in my_input:
        r.append(item*2)
    return r 

# However, multiplu_by_2_print is not a fp
# since it print sth that affect the world outside of it
def multiplu_by_2_print(my_input):
    r = []
    for item in my_input:
        r.append(item*2)
    print (r)


print (multiplu_by_2([1,2,3]))
print (multiplu_by_2_print([1,2,3]))