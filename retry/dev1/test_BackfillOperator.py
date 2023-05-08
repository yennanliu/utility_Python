import datetime as dt
from BackfillOperator import backfill_operator

run_count_1 = 0
run_count_2 = 0

@backfill_operator(max_run=10)
def my_etl_func1():

    global run_count_1
    run_count_1 += 1
    #print(f"run_count = {run_count_1}")
    return dt.timedelta(seconds=30)

@backfill_operator(max_run=0)
def my_etl_func2():

    global run_count_2
    run_count_2 += 1
    #print(f"run_count = {run_count_2}")
    return dt.timedelta(seconds=30)

def test_run_count_should_equal_one():

    my_etl_func1()
    assert run_count_1 == 10

    my_etl_func1()
    assert run_count_2 == 0

if __name__ == '__main__':
    test_run_count()
