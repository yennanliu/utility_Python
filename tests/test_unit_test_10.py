import unittest
from unittest.mock import patch, Mock
from my_db_utils import get_db_conn, sqlalchemy
from sqlalchemy.exc import DatabaseError


class TestMyFunc(unittest.TestCase):

    @patch('my_db_utils.sqlalchemy')
    def test_my_call_api_func(self, mock_sqlalchemy):
        mock_sqlalchemy.create_engine.side_effect = DatabaseError
        #with self.assertRaises(DatabaseError):
            #get_db_conn("abc", "def", "ijk")
        get_db_conn()
        mock_sqlalchemy.create_engine.assert_called_once()


if __name__ == '__main__':
    unittest.main()
