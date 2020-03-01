"""
Python dict comprehension demo 1 

comprehension can make code simple/elegent, but beware of the tradeoff between readability and simplicity 
"""
sample_dict = {
    
    'a' : 1,
    'b' : 2,
    'c' : 3
}

my_dict1 = { key:value for key, value in sample_dict.items()}
my_dict2 = { key:value**2 for key, value in sample_dict.items()}
my_dict3 = { key:value  for key, value in sample_dict.items() if value%2==0}

print (my_dict1)
print (my_dict2)
print (my_dict3)