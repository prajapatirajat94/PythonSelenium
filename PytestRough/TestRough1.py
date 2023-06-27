import pytest



#her we have pass input_total method in method parameter so it will run before each method



def test_total_divisionby_5(input_total):
    print("Division by 5")
    assert input_total%5 == 0

def test_total_divisionby_10(input_total):
    print("Division by 10")
    assert input_total%10 == 0

def test_total_divisionby_9(input_total):
    print("Division by 9")
    assert input_total%9 == 0


# python -m pytest TestRough1.py -v  --html=fix.html

