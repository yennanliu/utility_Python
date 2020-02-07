"""
extend "list" functionality in python 
"""
class SuperList(list): ### inherent default "list" ffunctionality here ###
    def __len__(self): 
        return 1000

super_list1 = SuperList()
print (len(super_list1)) 
super_list1.append(5) # SuperList has the list "append" method inherented from list
print (super_list1[0])
print (issubclass(SuperList, list))