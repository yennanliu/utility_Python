import pytest 

@pytest.fixture
def before_test():
    print (">>> befor test")

def test_1():
    assert 1 == 1

@pytest.fixture
def input_value():
    input = 39
    return input 


def test_divisible_by_3(input_value):
    assert input_value %  3 == 0 

def test_input_value(input_value):
    assert  input_value == 39


if __name__ == '__main__':
    pytest.main([__file__])