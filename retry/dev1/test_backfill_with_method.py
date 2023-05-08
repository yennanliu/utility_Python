import datetime as dt
from BackfillOperator import backfill_operator

run_count_1 = 0
run_count_2 = 0
run_count_3 = 0

delta_second_3 = 10

@backfill_operator(max_run=10)
def my_etl_func1():

    global run_count_1
    run_count_1 += 1
    return dt.timedelta(seconds=30)

@backfill_operator(max_run=0)
def my_etl_func2():

    global run_count_2
    run_count_2 += 1
    return dt.timedelta(seconds=30)

@backfill_operator(max_run=10, min_data_lag_to_stop=dt.timedelta(seconds=5), latest_time_for_rerun=dt.timedelta(seconds=1 + 100))
def my_etl_func3():

    global run_count_3
    global delta_second_3
    run_count_3 += 1
    delta_second_3 -= 1
    return dt.timedelta(seconds=delta_second_3)

def test_count_equals_ten():

    my_etl_func1()
    assert run_count_1 == 10

def test_count_equals_zero():

    my_etl_func1()
    assert run_count_2 == 0

def test_count_equals_five():

    my_etl_func3()
    assert run_count_3 == 5
