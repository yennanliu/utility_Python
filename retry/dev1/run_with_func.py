import datetime as dt
import time
import logging
from BackfillOperator import backfill_operator
from LogConfig import config_log

logger = logging.getLogger("main")
run_count = 0
run_count_1 = 0

MAX_RUN = 20
DEFAULT_DATA_LAG = dt.timedelta(seconds=1)
OFFSET_AFTER_RUN_ETL = dt.timedelta(seconds=1)

data_delta = 10
data_delta_1 = 10

@backfill_operator(max_run=10)
def dummy_etl_func_1():

    #print("dummy_etl_func_1 run")
    global run_count
    run_count += 1
    logger.info(f"run_count = {run_count}")
    return dt.timedelta(seconds=30)


#@backfill_operator(max_run=10)
@backfill_operator(max_run=MAX_RUN, min_data_lag_to_stop=DEFAULT_DATA_LAG)
#@backfill_operator(max_run=MAX_RUN, min_data_lag_to_stop=DEFAULT_DATA_LAG, latest_time_for_rerun=OFFSET_AFTER_RUN_ETL)
#@backfill_operator()
def dummy_etl_func_2():

    #print("dummy_etl_func_2 run")
    global run_count
    global data_delta
    run_count += 1
    logger.info(f"run_count = {run_count}")
    data_delta -= 1
    return dt.timedelta(seconds=data_delta)



@backfill_operator(max_run=10, 
    min_data_lag_to_stop=dt.timedelta(seconds=1000), 
    latest_time_for_rerun=dt.timedelta(seconds=1 + 1))
def dummy_etl_func_3():

    #print("dummy_etl_func_2 run")
    global run_count_1
    global data_delta_1
    run_count_1 += 1
    logger.info(f"(dummy_etl_func_3) run_count = {run_count_1}")
    data_delta_1 -= 1
    return dt.timedelta(seconds=data_delta_1)


@backfill_operator(max_run=10)
def dummy_etl_func_4():

    #print("dummy_etl_func_1 run")
    global run_count
    run_count += 1
    time.sleep(1)
    logger.info(f"run_count = {run_count}")
    return dt.timedelta(seconds=30)

def main():

    config_log()
    #dummy_etl_func_1()
    #dummy_etl_func_2()
    #dummy_etl_func_3()
    dummy_etl_func_4()

if __name__ == '__main__':
    start_time = dt.datetime.utcnow()
    main()
    end_time = dt.datetime.utcnow()
    time_diff_sec = (end_time - start_time).total_seconds()
    print(f"--> start_time = {start_time}, end_time = {end_time}, time_diff_sec = {time_diff_sec}")