import re

# https://regex101.com/
pattern = re.compile(r"[A-Za-z0-9$%#@]{7,}[0-9]")
mystring = 'accd1234'

a = pattern.fullmatch(mystring)
print (a)