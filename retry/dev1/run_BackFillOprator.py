import datetime as dt
from BackfillOperator import backfill_operator



@backfill_operator(max_run=10)
def my_dummy_func1():
    return None


@backfill_operator(max_run=10)
def my_dummy_func2():
    return 123

@backfill_operator(max_run=10, 
        min_data_lag_to_stop=dt.timedelta(seconds=1 + 1), 
        latest_time_for_rerun=100)
def my_dummy_func3():
    return 123

if __name__ == '__main__':
    #my_dummy_func1()
    #my_dummy_func2()
    my_dummy_func3()