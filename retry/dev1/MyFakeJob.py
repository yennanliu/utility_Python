import datetime as dt
import logging
import math
import time

logger = logging.getLogger(__name__)

DEFAULT_STOP_THRESHOLD = 0.5

"""
    Fake ETL class

    init_data_lag : initial data lag (lag that ETL needs to catchup)
    etl_process_time : time period for ETL job
    offset_after_run_etl :  offset after ETL executed, consider as extra time cost (e.g. DB slowness, client slow response ...)

"""
class MyFakeETL:

    def __init__(self, init_data_lag, etl_process_time, offset_after_run_etl, stop_threshold=DEFAULT_STOP_THRESHOLD):
        
        self._timestamp_of_last_etl_run = self.get_cur_time() - init_data_lag
        self._etl_process_time = etl_process_time
        self._offset_after_run_etl = offset_after_run_etl
        self._stop_threshold = stop_threshold

    def run_etl(self):

        logger.debug(f"Current data lag : {self.current_data_lag}")
        if abs(self.current_data_lag.total_seconds()) < self._stop_threshold:
            print("Nothing to run, exit ...")
            return dt.timedelta(seconds=0)

        logger.info("--> Run ETL start ...")
        self._run_etl()
        logger.info(f"Run ETL end ... current data lag: {self.current_data_lag}")
        return self.get_time_left()

    def _run_etl(self):

        # simulate etl process time, can use time-machine as next step : https://pypi.org/project/time-machine/
        sec_to_sleep = self._etl_process_time.total_seconds()
        logger.info(f"Sleep for {sec_to_sleep} seconds")
        time.sleep(sec_to_sleep)

        time_left = self.get_time_left()

        self._timestamp_of_last_etl_run += dt.timedelta(seconds = 
            min(time_left.total_seconds(), self._offset_after_run_etl.total_seconds())
        )

    @property
    def current_data_lag(self):
        return self.get_cur_time() - self._timestamp_of_last_etl_run

    def get_cur_time(self):
        return dt.datetime.utcnow()

    def get_time_left(self):
        return self.get_cur_time() - self._timestamp_of_last_etl_run