import datetime as dt
from BackfillOperator import backfill_operator
from MyFakeJob import MyFakeETL

run_count_1 = 0
run_count_2 = 0
run_count_3 = 0
run_count_4 = 0

def test_should_run_one_time():

    class MyETL1(MyFakeETL):

        @backfill_operator()
        def run_etl(self):

            global run_count_1
            run_count_1 += 1
            return super().run_etl()

    etl =  MyETL1(
        init_data_lag=dt.timedelta(seconds=15),
        etl_process_time=dt.timedelta(seconds=1),
        offset_after_run_etl=dt.timedelta(seconds=1 + 8)
    )

    etl.run_etl()

    assert run_count_1 == 1

def test_should_run_ten_time():


    class MyETL2(MyFakeETL):

        @backfill_operator(max_run=10)
        def run_etl(self):

            global run_count_2
            run_count_2 += 1
            print(f"MyETL2 run_etl, count = {run_count_2}")
            return super().run_etl()


    etl =  MyETL2(
        init_data_lag=dt.timedelta(seconds=20),
        etl_process_time=dt.timedelta(seconds=3),
        offset_after_run_etl=dt.timedelta(seconds=1 + 1)
    )

    etl.run_etl()

    assert run_count_2 == 10

def test_should_run_ten_time2():

    class MyETL3(MyFakeETL):

        @backfill_operator(max_run=10)
        def run_etl(self):

            global run_count_3
            run_count_3 += 1
            return super().run_etl()

    etl =  MyETL3(
        init_data_lag=dt.timedelta(seconds=0),
        etl_process_time=dt.timedelta(seconds=3),
        offset_after_run_etl=dt.timedelta(seconds=1 + 1)
    )

    etl.run_etl()

    assert run_count_3 == 1

def test_should_run_five_time():


    class MyETL4(MyFakeETL):

        @backfill_operator(max_run=10)
        def run_etl(self):

            global run_count_4
            run_count_4 += 1
            return super().run_etl()

    etl =  MyETL4(
        init_data_lag=dt.timedelta(seconds=14),
        etl_process_time=dt.timedelta(seconds=2),
        offset_after_run_etl=dt.timedelta(seconds=1 + 2)
    )

    etl.run_etl()

    assert run_count_4 == 5