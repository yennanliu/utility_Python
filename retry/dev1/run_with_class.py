import datetime as dt
import logging
from BackfillOperator import backfill_operator
from MyFakeJob import MyFakeETL
from LogConfig import config_log

logger = logging.getLogger("main")
run_count = 0
run_count_2 = 0
run_count_3 = 0
run_count_4 = 0
delta_second_1 = 0


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


class FakeETL4(MyFakeETL):

    @backfill_operator(max_run=10, min_data_lag_to_stop=dt.timedelta(seconds=5), latest_time_for_rerun=dt.timedelta(seconds=1 + 100))
    def run_etl(self):

        global run_count_3
        global delta_second_1
        run_count_3 += 1
        delta_second_1 -= 1
        print(f"run_count_3 = {run_count_3}")
        return super().run_etl()


class FakeETL5(MyFakeETL):

    @backfill_operator(max_run=10, 
        min_data_lag_to_stop=dt.timedelta(seconds=1), 
        latest_time_for_rerun=dt.timedelta(seconds=1 + 30))
    def run_etl(self):

        global run_count_4
        print(f"--> run_count_4 = {run_count_4}")
        run_count_4 += 1
        return super().run_etl()

def main():

    config_log()
    #etl_classes = [FakeETL1, FakeETL2]
    etl_classes = [FakeETL5]
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

        # etl =  etl_class(
        # init_data_lag=dt.timedelta(seconds=100),
        # etl_process_time=dt.timedelta(seconds=10),
        # offset_after_run_etl=dt.timedelta(seconds=1 + 1)
        # )

        # etl =  etl_class(
        # init_data_lag=dt.timedelta(seconds=12),
        # etl_process_time=dt.timedelta(seconds=0.5),
        # offset_after_run_etl=dt.timedelta(seconds=2),
        # stop_threshold = 3
        # )

        etl =  etl_class(
            init_data_lag=dt.timedelta(seconds=1000),
            etl_process_time=dt.timedelta(seconds=2),
            offset_after_run_etl=dt.timedelta(seconds=1 + 4)
        )


        etl.run_etl()

if __name__ == '__main__':
    main()
