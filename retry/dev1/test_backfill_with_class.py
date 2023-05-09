import datetime as dt
from BackfillOperator import backfill_operator
from MyFakeJob import MyFakeETL

run_count_1 = 0
run_count_2 = 0

class MyETL1(MyFakeETL):

    @backfill_operator()
    def run_etl(self):

        global run_count_1
        run_count_1 += 1
        return super().run_etl()


class MyETL2(MyFakeETL):

    @backfill_operator(max_run=10)
    def run_etl(self):

        global run_count_2
        run_count_2 += 1
        print(f"MyETL2 run_etl, count = {run_count_2}")
        return super().run_etl()

def test_class_count_equals_five():

    etl =  MyETL1(
        init_data_lag=dt.timedelta(seconds=15),
        etl_process_time=dt.timedelta(seconds=1),
        offset_after_run_etl=dt.timedelta(seconds=1 + 8)
    )

    etl.run_etl()

    assert run_count_1 == 1

def test_class_count_equals_ten():

    etl =  MyETL2(
        init_data_lag=dt.timedelta(seconds=20),
        etl_process_time=dt.timedelta(seconds=3),
        offset_after_run_etl=dt.timedelta(seconds=1 + 1)
    )

    etl.run_etl()

    assert run_count_2 == 10