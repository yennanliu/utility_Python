"""
extend "list" functionality in python 
"""
class SuperList(list): ### inherent default "list" functionality via "SuperList(list)" ###
    def __len__(self): # overwride the default "list" "len" method
        return 1000

print (">>> inherent/overwride default 'list' class")
super_list1 = SuperList()
print (len(super_list1)) # the "len" method has already been overwrote, so it will return 1000 instead of length of list
super_list1.append(5) # SuperList has the list "append" method inherented from list
print (super_list1[0])
print (issubclass(SuperList, list))

print (">>> default 'list' class")
x = list([1,2,3])
x.append(5)
print (x, len(x))