import re

pattern = re.compile('this')
mystring = 'search how many this in this line text'

a = pattern.search(mystring)
b = pattern.findall(mystring)
c = pattern.fullmatch(mystring)
c_ = pattern.match(mystring)
print (a)
print (b)
print (c)
print (c_)

pattern_ = re.compile(mystring)
d = pattern_.fullmatch(mystring)
print (d)