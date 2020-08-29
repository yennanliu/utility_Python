class myBaseClass:
    def get_name(self):
        print ("ths is my name")

    def print_sth(self):
        for i in range(5):
            print (i)

# inherit from myBaseClass
class myRunner(myBaseClass):
    def run(self):
        self.get_name()
        # run the print_sth in myBaseClass
        super().print_sth()

    # re-write the print_sth method from myBaseClass    
    def print_sth(self):
        print ("this is print_sth in myRunner")

myrun = myRunner()
myrun.run()
myrun.print_sth()