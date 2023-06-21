import pytest

def test_M3():
    return True

@pytest.mark.login
def test_M4():
    assert 100==100,"Test Passed"

def test_M5():
    assert "naveen"=="naveen","Test Passed"

def test_login():
    assert "login"=="login"