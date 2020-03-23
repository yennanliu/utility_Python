"""
Mock the sqlalchemy.create_engine method,
and test create_db_engine via above mock 

"""
import unittest
from unittest.mock import patch, Mock

# Mock sqlalchemy method
sqlalchemy = Mock()

def create_db_engine():
    # TODO : mock create_db_engine with db conn param 
    # conn = sqlalchemy.create_engine(
    #     host = "my_host",
    #     port = "my_port",
    #     user = "my_user",
    #     db = "my_database")
    conn = sqlalchemy.create_engine()
    if conn.status_code == 200:
        return conn.json()
        # TODO : mock cursor, cursor.execute.. 
        # cursor = conn.cursor()
        # data = cursor.execute(query)
        # return data
    return None

class TestMock(unittest.TestCase):

    def fake_response(self):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {'response': '123'}
        return response_mock

    def test_create_db_engine(self):
        sqlalchemy.create_engine.side_effect = self.fake_response
        assert create_db_engine()['response'] == '123'

if __name__ == '__main__':
    unittest.main()
