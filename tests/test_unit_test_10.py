"""
* use patch() as a decorator

mock my_db_utils.sqlalchemy
and test if 
    - mock_sqlalchemy.create_engine.side_effec
    - mock_sqlalchemy.get_conn.return_value
work as expected
"""
import unittest
from unittest.mock import patch, Mock
from my_db_utils import get_db_conn, sqlalchemy
from sqlalchemy.exc import DatabaseError


class TestMyFunc(unittest.TestCase):

    @patch('my_db_utils.sqlalchemy')
    def test_get_db_conn(self, mock_sqlalchemy):
        mock_sqlalchemy.create_engine.side_effect = DatabaseError
        mock_sqlalchemy.get_conn.return_value = "db_conn"
        get_db_conn()

        mock_sqlalchemy.create_engine.assert_called_once()
        assert mock_sqlalchemy.get_conn() == "db_conn"


if __name__ == '__main__':
    unittest.main()
