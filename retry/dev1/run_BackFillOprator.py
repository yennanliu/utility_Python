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


@backfill_operator(max_run=-1)
def my_dummy_func4():
    return 123

@backfill_operator(min_data_lag_to_stop=dt.timedelta(seconds=-100))
def my_dummy_func5():
    return dt.timedelta(seconds=1)

@backfill_operator()
def my_dummy_func6():
    return dt.timedelta(seconds=-1)

if __name__ == '__main__':
    #my_dummy_func1()
    #my_dummy_func2()
    #my_dummy_func3()
    #my_dummy_func4()
    #my_dummy_func5()
    my_dummy_func6()