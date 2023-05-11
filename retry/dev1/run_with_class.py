import datetime as dt
import logging
from BackfillOperator import backfill_operator
from MyFakeJob import MyFakeETL
from LogConfig import config_log

logger = logging.getLogger("main")
run_count = 0
run_count_2 = 0

class FakeETL1(MyFakeETL):

    @backfill_operator(max_run=20, min_data_lag_to_stop=dt.timedelta(seconds=1))
    def run_etl(self):
        return super().run_etl()


class FakeETL2(MyFakeETL):

    @backfill_operator()
    def run_etl(self):
        return super().run_etl()


class FakeETL3(MyFakeETL):

    @backfill_operator(max_run=10, min_data_lag_to_stop=dt.timedelta(seconds=10))
    def run_etl(self):

        global run_count_2
        run_count_2 += 1
        print(f"FakeETL3 run_etl, count = {run_count_2}")
        return super().run_etl()

def main():

    config_log()
    #etl_classes = [FakeETL1, FakeETL2]
    etl_classes = [FakeETL3]
    for etl_class in etl_classes:
        logger.info(f"ETL = {etl_class}")
        # etl = etl_class(
        #     init_data_lag=dt.timedelta(seconds=15),
        #     etl_process_time=dt.timedelta(seconds=1),
        #     offset_after_run_etl=dt.timedelta(seconds=1 + 8)
        # )
        # etl = etl_class(
        #     init_data_lag=dt.timedelta(seconds=14),
        #     etl_process_time=dt.timedelta(seconds=2),
        #     offset_after_run_etl=dt.timedelta(seconds=1 + 2)
        # )

        etl =  etl_class(
        init_data_lag=dt.timedelta(seconds=100),
        etl_process_time=dt.timedelta(seconds=10),
        offset_after_run_etl=dt.timedelta(seconds=1 + 1)
        )

        etl.run_etl()

if __name__ == '__main__':
    main()
