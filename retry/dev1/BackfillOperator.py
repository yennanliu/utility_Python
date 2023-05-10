import datetime as dt
import functools
import logging

DEFAULT_MAX_RUN = 10
DEFAULT_DATA_LAG_TO_STOP = dt.timedelta(seconds=10)

logger = logging.getLogger(__name__)

"""
    decorator offers auto rerun in order to backfill data

    _func : the func need to be rerun
    max_run : max times to rerun
    min_data_lag_to_stop : minimum time difference to stop rerun, means data delay is acceptable
    latest_time_for_rerun : max time for rerun, if execution time > latest_time_for_rerun, then exit rerun
"""
def backfill_operator(_func = None, *, max_run = DEFAULT_MAX_RUN, min_data_lag_to_stop = DEFAULT_DATA_LAG_TO_STOP, latest_time_for_rerun = None):

    def decorator_rerun(func):

        logger.info(f">>> (decorator_rerun) func = {func}")

        number_of_run = 0
        timestamp_run_started = None

        def if_stop_rerun(current_data_lag):

            logger.info(f"(backfill_operator) current_data_lag = {current_data_lag}, min_data_lag_to_stop = {min_data_lag_to_stop}")

            # max run reached
            if max_run and (number_of_run >= max_run):
                logger.info(f"Max count of return reached, exit backfill process. Nunmber of run : {number_of_run}. Max run : {max_run}")
                return True

            # data lag is acceptable
            if (min_data_lag_to_stop) and (current_data_lag <= min_data_lag_to_stop):
                logger.info(f"Current data lag is OK, exit backfill process. Data lag : {current_data_lag}. min_data_lag_to_stop = {min_data_lag_to_stop}")
                return True

            # if rerun time > max time for rerun
            if latest_time_for_rerun and timestamp_run_started:
                run_time = dt.datetime.utcnow() - timestamp_run_started
                logger.info(f">>> run_time = {run_time}, latest_time_for_rerun = {latest_time_for_rerun}")
                if run_time >= latest_time_for_rerun:
                    logger.info(f"Latest rerun time is exhausted, exit backfill process"
                                f"Latest time for rerun : {latest_time_for_rerun}."
                                f"Run time : {run_time}"
                    )
                    return True

            return False

        @functools.wraps(func)
        def wrapper_rerun(*args, **kwargs):

            #print(">>> wrapper_rerun")
            #logger.info(f"(>>> (wrapper_repeat) func = {str(func)}")

            nonlocal number_of_run
            nonlocal timestamp_run_started

            number_of_run = 0

            timestamp_run_started = dt.datetime.utcnow()

            while True:
                print(f">>> func = {func}")
                current_data_lag = func(*args, **kwargs)
                number_of_run += 1

                if if_stop_rerun(current_data_lag=current_data_lag):
                    logger.info(">>> (wrapper_rerun) break")
                    break

            return current_data_lag

        return wrapper_rerun

    if _func is None:
        return decorator_rerun
    return decorator_rerun(_func)
