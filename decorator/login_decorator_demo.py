#################################################################
# SCRIPT DEMO HOW TO SIMULATE LOGIN OPERATION VIA CACHE  
#################################################################

# V0 
# https://www.geeksforgeeks.org/class-as-decorator-in-python/
# https://stackoverflow.com/questions/22170848/simple-login-program-in-python
class login:
    def __init__(self, id, pas):
        self.id = id
        self.pas = pas

    def check(self, id, pas):
        #print (self.id)
        if self.id == id and self.pas == pas:
            print ("Login success!")
        else:
            print ('Login failed!')

# # example 1 
# log = login("admin", "admin")
# log.check('2342',
#           '32rr423')
# output 
# Login failed!
# # example 2 
# log = login("admin", "admin")
# log.check('admin',
#           'admin')
# output
# Login success!

# V1 
class LOGIN: 
    def __init__(self, function): 
        self.function = function 
      
    def __call__(self): 
  
        password = self.function() 
        print ('password :', password)
        if password == 'password':
            print ('login ok')
        else:
            print ('login failed')
  
# adding decorator to the class 
@LOGIN
def function(): 
	print ('test login')
    return 'password' 
function()  
# output 
# test login
# password : password
# login ok
