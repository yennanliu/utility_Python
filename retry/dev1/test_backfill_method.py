import datetime as dt
from BackfillOperator import backfill_operator
import time

run_count_1 = 0
run_count_2 = 0
run_count_3 = 0
run_count_4 = 0
run_count_5 = 0
run_count_6 = 0
run_count_7 = 0
delta_second_1 = 10
delta_second_2 = 10

def test_run_one_time_when_delay_in_range():

    @backfill_operator(max_run=10, min_data_lag_to_stop=dt.timedelta(seconds=10))
    def my_etl_func():

        global run_count_1
        run_count_1 += 1
        return dt.timedelta(seconds=1)

    my_etl_func()
    assert run_count_1 == 1


def test_run_ten_times_when_delay_out_of_range():

    @backfill_operator(max_run=10, min_data_lag_to_stop=dt.timedelta(seconds=10))
    def my_etl_func():

        global run_count_2
        run_count_2 += 1
        return dt.timedelta(seconds=20)

    my_etl_func()
    assert run_count_2 == 10


def test_should_run_max_ten_times_if_cant_catch_up():

    @backfill_operator(max_run=10, min_data_lag_to_stop=dt.timedelta(seconds=10))
    def my_etl_func():

        global run_count_3
        run_count_3 += 1
        return dt.timedelta(seconds=15)

    my_etl_func()
    assert run_count_3 <= 10

def test_should_run_ten_times_as_default():

    @backfill_operator()
    def my_etl_func():

        global run_count_4
        run_count_4 += 1
        return dt.timedelta(seconds=30)

    my_etl_func()
    assert run_count_4 == 10

def test_should_run_five_times_if_can_catchup():

    @backfill_operator(max_run=10, 
        min_data_lag_to_stop=dt.timedelta(seconds=5), 
        latest_time_for_rerun=dt.timedelta(seconds=1 + 100))
    def my_etl_func():

        global run_count_5
        global delta_second_1
        run_count_5 += 1
        delta_second_1 -= 1
        return dt.timedelta(seconds=delta_second_1)

    my_etl_func()
    assert run_count_5 == 5


def test_should_run_no_more_than_hundred_times():

    @backfill_operator(max_run=100)
    def my_etl_func():

        global run_count_6
        run_count_6 += 1
        return dt.timedelta(seconds=1000)

    my_etl_func()
    assert run_count_6 <= 100

def test_should_run_one_time_if_no_need_to_catchup():

    @backfill_operator(max_run=10, 
        min_data_lag_to_stop=dt.timedelta(seconds=1000), 
        latest_time_for_rerun=dt.timedelta(seconds=1 + 1))
    def my_etl_func():

        global run_count_7
        global delta_second_2
        run_count_7 += 1
        delta_second_2 -= 1
        return dt.timedelta(seconds=delta_second_2)

    my_etl_func()
    assert run_count_7 == 1


def test_should_run_in_defined_duration():

    run_count = 0

    @backfill_operator(max_run=5, 
        min_data_lag_to_stop=dt.timedelta(seconds=1), 
        latest_time_for_rerun=dt.timedelta(seconds=1 + 10))
    def my_etl_func():

        nonlocal run_count
        run_count += 1
        time.sleep(1)
        return dt.timedelta(seconds=1000)

    start_time = dt.datetime.utcnow()
    my_etl_func()
    end_time = dt.datetime.utcnow()
    time_diff_sec = (end_time - start_time).total_seconds()
    assert int(time_diff_sec) == 5
