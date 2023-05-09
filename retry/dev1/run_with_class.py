import datetime as dt
import logging
from BackfillOperator import backfill_operator
from MyFakeJob import MyFakeETL
from LogConfig import config_log

logger = logging.getLogger("main")
run_count = 0


class FakeETL1(MyFakeETL):

    @backfill_operator(max_run=20, min_data_lag_to_stop=dt.timedelta(seconds=1))
    def run_etl(self):
        return super().run_etl()


class FakeETL2(MyFakeETL):

    @backfill_operator()
    def run_etl(self):
        return super().run_etl()


def main():

    config_log()
    #etl_classes = [FakeETL1, FakeETL2]
    etl_classes = [FakeETL1]
    for etl_class in etl_classes:
        logger.info(f"ETL = {etl_class}")
        # etl = etl_class(
        #     init_data_lag=dt.timedelta(seconds=15),
        #     etl_process_time=dt.timedelta(seconds=1),
        #     offset_after_run_etl=dt.timedelta(seconds=1 + 8)
        # )
        etl = etl_class(
            init_data_lag=dt.timedelta(seconds=14),
            etl_process_time=dt.timedelta(seconds=2),
            offset_after_run_etl=dt.timedelta(seconds=1 + 2)
        )
        etl.run_etl()

if __name__ == '__main__':
    main()
