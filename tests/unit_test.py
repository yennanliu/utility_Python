import unittest
import sys
sys.path.append(".")
sys.path.append("./mydevclass")
from mydevclass import code_to_test
import mock

class CodeToTestTestCase(unittest.TestCase):
    @mock.patch('code_to_test.sqlite3.connect')
    def test_database_drop_table_call(self, mock_sqlite3_connect):
        sqlite_execute_mock = mock.Mock()
        mock_sqlite3_connect.return_value = sqlite_execute_mock
        code_to_test.main()
        call = 'drop table if exists some_table;'
        sqlite_execute_mock.execute.assert_called_with(call)

if __name__ == '__main__':
    pytest.main([__file__])