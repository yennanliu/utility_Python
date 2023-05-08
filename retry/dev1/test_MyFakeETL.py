import datetime as dt

from MyFakeJob import MyFakeETL


def main():

    fake_etl = MyFakeETL(
        init_data_lag=dt.timedelta(seconds=15),
        time_to_run_etl=dt.timedelta(seconds=1),
        offlest_after_run_etl=dt.timedelta(seconds=1 + 8)
    )

    print(f"fake_etl = {fake_etl}, current_data_lag = {str(fake_etl.get_cur_time())}, get_time_left = {str(fake_etl.get_time_left())}")
    fake_etl.run_etl()
    fake_etl.run_etl()
    fake_etl.run_etl()

if __name__ == '__main__':
    main()