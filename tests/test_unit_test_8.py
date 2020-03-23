"""
Use Mock method mock method, 
and use it (mock) test other need-to-test method

"""
import unittest
from unittest.mock import patch, Mock

# Mock requests method
requests = Mock()


def call_api():
    r = requests.get('http://my_web/api/get_something')
    if r.status_code == 200:
        return r.json() 
    return None

class TestMock(unittest.TestCase):

    def fake_response(self, url):
        print (">>> call fake_response")
        # mock response_mock method
        response_mock = Mock()
        # mock response_mock's status_code as 200
        response_mock.status_code = 200 
        # mock status_code.json's return value =  {'item1': 'abc','item2': 'def',}
        response_mock.json.return_value = {
            'item1': 'abc',
            'item2': 'def',
        }
        return response_mock

    def test_call_api(self):
        # mock requests.get return as self.fake_response (via mock side_effect)
        requests.get.side_effect = self.fake_response
        assert call_api()['item1'] == 'abc'

if __name__ == '__main__':
    unittest.main()