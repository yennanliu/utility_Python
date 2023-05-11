import datetime as dt
from BackfillOperator import backfill_operator
from MyFakeJob import MyFakeETL

run_count_1 = 0
run_count_2 = 0
run_count_3 = 0
run_count_4 = 0

def test_run_one_time_when_delay_in_range():

    class MyETL(MyFakeETL):

        @backfill_operator(max_run=10, min_data_lag_to_stop=dt.timedelta(seconds=10))
        def run_etl(self):

            global run_count_1
            run_count_1 += 1
            return super().run_etl()

    etl =  MyETL(
        init_data_lag=dt.timedelta(seconds=5),
        etl_process_time=dt.timedelta(seconds=1),
        offset_after_run_etl=dt.timedelta(seconds=1 + 1)
    )

    etl.run_etl()
    assert run_count_1 == 1

def test_run_ten_times_when_delay_out_of_range():


    class MyETL(MyFakeETL):

        @backfill_operator(max_run=10, min_data_lag_to_stop=dt.timedelta(seconds=10))
        def run_etl(self):

            global run_count_2
            run_count_2 += 1
            print(f"MyETL2 run_etl, count = {run_count_2}")
            return super().run_etl()

    etl =  MyETL(
        init_data_lag=dt.timedelta(seconds=100),
        etl_process_time=dt.timedelta(seconds=3),
        offset_after_run_etl=dt.timedelta(seconds=1 + 1)
    )

    etl.run_etl()
    assert run_count_2 == 10

def test_should_run_max_ten_times_if_cant_catch_up():

    class MyETL(MyFakeETL):

        @backfill_operator(max_run=10, min_data_lag_to_stop=dt.timedelta(seconds=10))
        def run_etl(self):

            global run_count_3
            run_count_3 += 1
            return super().run_etl()

    etl =  MyETL(
        init_data_lag=dt.timedelta(seconds=15),
        etl_process_time=dt.timedelta(seconds=3),
        offset_after_run_etl=dt.timedelta(seconds=1 + 5)
    )

    etl.run_etl()
    assert run_count_3 <= 10

def test_should_run_ten_times_as_default():


    class MyETL(MyFakeETL):

        @backfill_operator()
        def run_etl(self):

            global run_count_4
            run_count_4 += 1
            return super().run_etl()

    etl =  MyETL(
        init_data_lag=dt.timedelta(seconds=30),
        etl_process_time=dt.timedelta(seconds=2),
        offset_after_run_etl=dt.timedelta(seconds=1 + 0)
    )

    etl.run_etl()

    assert run_count_4 == 10