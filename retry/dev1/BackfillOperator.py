import datetime as dt
import functools
import logging

DEFAULT_MAX_RUN = 10
DEFAULT_DATA_LAG = dt.timedelta(seconds=10)

def backfill_operator(func = None, max_run = DEFAULT_MAX_RUN, min_data_lag_to_stop: DEFAULT_DATA_LAG, latest_time_for_rerun = None):

    def decorator_rerun(func):

        number_of_run = 0
        timestamp_run_started = None

        def if_stop_rerun(current_data_lag = dt.timedelta):

            # max run reached
            if max_run and (number_of_run > max_run):
                print(f"Max count of return reached, exit backfill process. Nunmber of run : {number_of_run}. Max run : {max_run}")
                return True

            # data lag is acceptable
            if (min_data_lag_to_stop) and (current_data_lag <= min_data_lag_to_stop):
                print(f"Current data lag is OK, exit backfill process. Data lag : {current_data_lag}")
                return True 

            # if rerun time > max time for rerun
            if latest_time_for_rerun and timestamp_run_started:
                run_time = dt.datetime.utcnow() - timestamp_run_started
                if run_time >= latest_time_for_rerun:
                    print(f"Latest rerun time is exhausted, exit backfill process. Latest time for rerun : {latest_time_for_rerun}. Run time : {run_time}")
                    return True

            return False

    @functools.wraps(func)
    def wrapper_rerun(*args, **kwargs):

        nonlocal number_of_run
        nonlocal timestamp_run_started

        timestamp_run_started = dt.datetime.utcnow()

        while True:
            current_data_lag = func(*args, **kwargs)
            number_of_run += 1

            if if_stop_rerun(current_data_lag=current_data_lag):
                break
        return current_data_lag

    if fun is None:
        log.warn(f"input func is Null")
        return decorator_rerun
    return decorator_rerun(_func)
