import datetime as dt
import logging
from BackfillOperator import backfill_operator
from LogConfig import config_log

logger = logging.getLogger("main")
run_count = 0


@backfill_operator(max_run=10)
def dummy_etl_func():

	print("dummy_etl_func run")
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