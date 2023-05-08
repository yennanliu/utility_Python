import datetime as dt
import logging
from MyFakeJob import MyFakeETL
from LogConfig import config_log

logger = logging.getLogger(__name__)

def main():

    config_log()

    fake_etl = MyFakeETL(
        init_data_lag=dt.timedelta(seconds=15),
        time_to_run_etl=dt.timedelta(seconds=1),
        offlest_after_run_etl=dt.timedelta(seconds=1 + 5)
    )

    logger.info(f"fake_etl = {fake_etl}, current_data_lag = {str(fake_etl.get_cur_time())}, get_time_left = {str(fake_etl.get_time_left())}")
    fake_etl.run_etl()
    fake_etl.run_etl()
    fake_etl.run_etl()

if __name__ == '__main__':
    main()