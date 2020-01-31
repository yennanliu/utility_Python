# https://pythonprogramminglanguage.com/overriding-methods/

class Robot:
    def action(self):
        print('Robot action')

class HelloRobot(Robot):
    def action(self):
        print('Hello world (override)')

class DummyRobot(Robot):
    def start(self):
        print('Started.')
        
if __name__ == '__main__':
    r = HelloRobot()
    d = DummyRobot()

    # run the override "action"
    r.action()
    # run the orignal "action", no override 
    d.action()