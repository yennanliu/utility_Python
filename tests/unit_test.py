import unittest
import pytest
import sys
sys.path.append(".")
sys.path.append("./mydevclass")
from mydevclass import code_to_test, code_to_test2, code_to_test3, code_to_test4
import mock

# @pytest.yield_fixture
# def mock_DB():
#     @mock.patch('obj.method')
#     return mockDB

class Test_CodeToTest_1(unittest.TestCase):
    @mock.patch('code_to_test.sqlite3.connect')
    def test_database_drop_table_call1(self, mock_sqlite3_connect):
        sqlite_execute_mock = mock.Mock()
        mock_sqlite3_connect.return_value = sqlite_execute_mock
        # test main
        code_to_test.main()
        call = 'drop table if exists some_table;'
        sqlite_execute_mock.execute.assert_called_with(call)

class Test_CodeToTest_2(unittest.TestCase):
    @mock.patch('code_to_test2.sqlite3.connect')
    def test_database_drop_table_call2(self, mock_sqlite3_connect):
        sqlite_execute_mock = mock.Mock()
        mock_sqlite3_connect.return_value = sqlite_execute_mock
        # test main 
        code_to_test2.main()
        call = 'select * from some_table;'
        sqlite_execute_mock.execute.assert_called_with(call)

class Test_CodeToTest_3(unittest.TestCase):
    @mock.patch('code_to_test3.sqlite3.connect')
    def test_database_drop_table_call3(self, mock_sqlite3_connect):
        sqlite_execute_mock = mock.Mock()
        mock_sqlite3_connect.return_value = sqlite_execute_mock

        # test select_from_db 
        code_to_test3.select_from_db()
        call = 'select * from some_table;'
        sqlite_execute_mock.execute.assert_called_with(call)

        # test drop_from_db
        code_to_test3.drop_from_db()
        call = 'drop table if exists some_table;'
        sqlite_execute_mock.execute.assert_called_with(call)

        # test insert_to_db
        code_to_test3.insert_to_db()
        call = '''INSERT INTO some_table(name,begin_date,end_date) VALUES(?,?,?) '''
        sqlite_execute_mock.execute.assert_called_with(call)

# class Test_CodeToTest_4(unittest.TestCase):
#     @mock.patch('code_to_test4.psycopg2.connect')
#     def test_database_drop_table_call4(self, mock_postgre_connect):
#         postgre_execute_mock = mock.Mock()
#         mock_postgre_connect.return_value = postgre_execute_mock
#         # test create_table 
#         code_to_test4.create_table()
#         call  = "CREATE TABLE {} {}".format("some_table", "some_schema")
#         call = execute('not called')
#         postgre_execute_mock.execute.assert_called_with(call)

if __name__ == '__main__':
    pytest.main([__file__])
