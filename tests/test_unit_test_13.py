# test_data_manipulator.py
import unittest
from unittest.mock import patch
import data_manipulator

# https://www.reddit.com/r/learnpython/comments/4ivjo7/unit_testing_a_function_that_writesreads_to/

# data_manipulator.py
# def get_data():
#     """Get data from database."""
#     return ["user", "password", 26]
# def save_data(data):
#     """Save data to the database, and return True if successful."""
#     return True
# def do_manipulation():
#     """Get data from the database, do manipulation, and save data back to the database."""
#     data = get_data()
#     if data:
#         # do manipulation here
#         return save_data(data)
#     else:
#         raise ValueError

class ManipulationTest(unittest.TestCase):
    mock_data_good = ["Rosco", "Dude", 99]
    mock_data_bad = []

    def test_do_manipulation(self):
        with patch.object(data_manipulator, "get_data", return_value=ManipulationTest.mock_data_good) as mocked_get, \
        patch.object(data_manipulator, "save_data", return_value=True) as mocked_save:
            result = data_manipulator.do_manipulation()
            self.assertTrue(result)

        with patch.object(data_manipulator, "get_data", return_value=ManipulationTest.mock_data_bad) as mocked_get, \
        patch.object(data_manipulator, "save_data") as mocked_save:
            with self.assertRaises(ValueError):
                result = data_manipulator.do_manipulation()

if __name__ == '__main__':
    unittest.main()
