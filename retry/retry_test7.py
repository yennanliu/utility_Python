from Rerun import rerun
import time, datetime

RERUN_INTERVAl = 2
TIME_DELTA = 20
MAX_RUN = 4
#TO_CATCH = datetime.datetime.now() + datetime.timedelta(seconds=TIME_DELTA)

# @rerun(to_catch_time=TO_CATCH, rerun_interval=RERUN_INTERVAl)
class MyClient:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print ('class init')

    def print(self):
        print (f'name = {self.name}, age = {self.age}')

    @classmethod
    def call_api(self):
        print('api call!')

def get_table_update_time():
    return datetime.datetime.now() + datetime.timedelta(seconds=TIME_DELTA)

def run():
    TO_CATCH = get_table_update_time()
    @rerun(to_catch_time=TO_CATCH, rerun_interval=RERUN_INTERVAl, max_rerun=MAX_RUN)
    def call():
        MyClient('tom', 33).call_api()
        #client.call_api()
    call()


if __name__ == '__main__':
    #client = MyClient('tom', 33)
    #client.show()
    run()
