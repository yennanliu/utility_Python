# https://docs.pytest.org/en/latest/fixture.html

import pytest

@pytest.fixture(scope="module")
def smtp_connection():
    import smtplib
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    yield smtp_connection
    print ("teardown smtp")
    smtp_connection.close()

def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    #assert 0  # for demo purposes


if __name__ == '__main__':
    pytest.main([__file__])