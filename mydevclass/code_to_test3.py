import sqlite3


def select_from_db():
    table_name = 'some_table'
    sqlite_db = sqlite3.connect('database.sqlite')
    sqlite_db.execute("select * from {};".format(table_name))

def drop_from_db():
    table_name = 'some_table'
    sqlite_db = sqlite3.connect('database.sqlite')
    sqlite_db.execute("drop table if exists {};".format(table_name))

if __name__ == '__main__':
    select_from_db()
    drop_from_db()