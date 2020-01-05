import sqlite3


def main():
    table_name = 'some_table'
    sqlite_db = sqlite3.connect('database.sqlite')
    sqlite_db.execute("drop table if exists {};".format(table_name))
    # next, get some data and then save to db

if __name__ == '__main__':
    main()