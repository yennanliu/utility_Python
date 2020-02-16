import re

# https://regex101.com/
pattern = re.compile(r"[a-z]")
mystring = 'search how many this in this line text'

a = pattern.search(mystring)
b = pattern.findall(mystring)
c = pattern.fullmatch(mystring)
c_ = pattern.match(mystring)
print (a)
print (b)
print (c)
print (c_)