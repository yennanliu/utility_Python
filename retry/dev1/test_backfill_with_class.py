import datetime as dt
from BackfillOperator import backfill_operator
from MyFakeJob import MyFakeETL

run_count_1 = 0

class MyETL1(MyFakeETL):

    @backfill_operator()
    def run_etl(self):
        global run_count_1
        run_count_1 += 1
        return super().run_etl()


def test_class_count_equals_five():
    #assert 1 == 1
    etl =  MyETL1(
        init_data_lag=dt.timedelta(seconds=15),
        time_to_run_etl=dt.timedelta(seconds=1),
        offlest_after_run_etl=dt.timedelta(seconds=1 + 8)
    )

    etl.run_etl()

    assert run_count_1 == 1