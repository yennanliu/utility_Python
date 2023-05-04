import time, datetime

def rerun(to_catch_time, rerun_interval, max_rerun):
    def real_decorator(decor_method):
        def _decorator(*args, **kwargs):
            current_time = datetime.datetime.now()
            count = 0
            #while current_time < to_catch_time:
            while current_time < to_catch_time and count < max_rerun:
            #while True:
                try:
                    print (f'Rerun: current_time = {current_time}, to_catch_time = {to_catch_time}, count = {count}')
                    time.sleep(rerun_interval)
                    count += 1
                    current_time += datetime.timedelta(seconds=rerun_interval)
                    return_values = decor_method(*args, **kwargs)
                    print (f'return_values = {return_values}')
                    #return return_values
                except Exception as error:
                    print (f'Error: current_time = {current_time}, to_catch_time = {to_catch_time}, count = {count}, exception = {error}')
        return _decorator
    return real_decorator