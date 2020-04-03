# Utility_Python

- `Collection of python working scripts` and `OOP` basic demo


### Development 

```bash
(ds_dash) yennanliu@yennanliu-MBP:~/utility_python(master⚡) » pytest -v tests

# ============================ test session starts =============================
# platform darwin -- Python 3.5.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- /Users/yennanliu/anaconda3/envs/ds_dash/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/yennanliu/utility_python
# plugins: celery-4.2.1
# collected 1 item                                                             

# tests/unit_test.py::CodeToTestTestCase::test_database_drop_table_call PASSED [100%]

# ========================== 1 passed in 0.05 seconds ==========================

```

### Ref 

- `Functional programming (fp)` VS `Object-oriented programming (OOP)`
	- https://www.coursera.org/lecture/programming-languages-part-c/oop-versus-functional-decomposition-mKEXO
	- https://stackoverflow.com/questions/2984460/do-you-use-python-mostly-for-its-functional-or-object-oriented-features

- Regular expression doc 
	- https://www.w3schools.com/python/python_regex.asp

- Regular expression online playground 
	- https://regex101.com/

- Regular expression tutorial
	- https://regexone.com/

- Python test tutorial
	- https://realpython.com/tutorials/testing/
	- Use a `decorator` : when all of the code in your test function body uses a mock.
	- Use a c`ontext manager` : when some of the code in your test function uses a mock and other code references the actual function.
	- Use a `patcher` :  when you need to explicitly start and stop mocking a function across multiple tests (e.g. the setUp() and tearDown() functions in a test class).

- Unit test mock DB func with python 
	- https://www.stevenmaude.co.uk/posts/how-to-use-mock-in-python-to-mock?fbclid=IwAR15w5IZesgbksFYkp_HBxMXRVk2ip1LMnZ6J3Jf4_LjXuaQLPzCNk1x_58
	- https://stackoverflow.com/questions/58873971/python-mock-multiple-queries-in-a-function-using-pytest-mock?fbclid=IwAR3Ouw0im_iFT6PBIclw5lLwNXs3lCTfayQdmZdYfYEpoFyLDmzHVMnf6zQ

- Python `Mock` library intro
	- https://realpython.com/python-mock-library/#patch
	- https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect
		- A `.return_value` defines what the method will return
		- A `.side_effect` defines what happens when you call the mocked function.

- Python `interface` intro
	- https://realpython.com/python-interface/

- pytest with fixture
	- https://docs.pytest.org/en/latest/fixture.html
