import datetime as dt
import logging
import math
import time

logger = logging.getLogger(__name__)

class MyFakeETL:

    def __init__(self, init_data_lag, time_to_run_etl, offset_after_run_etl):
        
        self._timestamp_of_last_etl_run = self.get_cur_time() - init_data_lag
        self._time_to_run_etl = time_to_run_etl
        self._offset_after_run_etl = offset_after_run_etl

    def run_etl(self):

        logger.debug(f"Current data lag : {self.current_data_lag}")
        if abs(self.current_data_lag.total_seconds()) < 0.5:
            print("Nothing to run, exit ...")
            return dt.timedelta(seconds=0)

        logger.info("--> Run ETL start ...")
        self._run_etl()
        logger.info(f"Run ETL end ... current data lag: {self.current_data_lag}")
        return self.get_time_left()

    def _run_etl(self):

        # simulate etl process time, can use time-machine as next step : https://pypi.org/project/time-machine/
        sec_to_sleep = self._time_to_run_etl.total_seconds()
        logger.info(f"Sleep for {sec_to_sleep} seconds")
        time.sleep(sec_to_sleep)

        time_left = self.get_time_left()

        self._timestamp_of_last_etl_run += dt.timedelta(seconds = min(time_left.total_seconds(), self._offset_after_run_etl.total_seconds()))

    @property
    def current_data_lag(self):
        return self.get_cur_time() - self._timestamp_of_last_etl_run

    def get_cur_time(self):
        return dt.datetime.utcnow()

    def get_time_left(self):
        return self.get_cur_time() - self._timestamp_of_last_etl_run