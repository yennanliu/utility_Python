import datetime as dt
import logging
from BackfillOperator import backfill_operator
from LogConfig import config_log

logger = logging.getLogger("main")
run_count = 0


MAX_RUN = 10
DEFAULT_DATA_LAG = dt.timedelta(seconds=10)
OFFSET_AFTER_RUN_ETL = dt.timedelta(seconds=10)

#@backfill_operator(max_run=10)
#@backfill_operator(max_run=MAX_RUN, min_data_lag_to_stop=DEFAULT_DATA_LAG)
@backfill_operator(max_run=MAX_RUN, min_data_lag_to_stop=DEFAULT_DATA_LAG, latest_time_for_rerun=OFFSET_AFTER_RUN_ETL)
#@backfill_operator()
def dummy_etl_func():

	#print("dummy_etl_func run")
	global run_count
	run_count += 1
	logger.info(f"run_count = {run_count}")
	#return dt.timedelta(hours=10)
	#return dt.timedelta(seconds=10)
	return dt.timedelta(minutes=10)

def main():

    config_log()
    #logger.debug(f"func_name: {dummy_etl_func.__name__}")
    dummy_etl_func()

if __name__ == '__main__':
    main()