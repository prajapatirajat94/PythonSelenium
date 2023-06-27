import pytest

#start with test
#End with test
# Function names which are not of format test* are not considered as test functions by pytest.
# We cannot explicitly make pytest consider any function not starting with test as a test function.
#1.file name has to be start or End with test
#2.function name also has to be start with test otherwise python will not recognized
#To run test from command line run -> python -m pytest

#if you want to run pertcular test which contain some text then := python -m pytest -k "Text" -v
#Marker in python command line ->  python -m pytest -m login
# if want to run from perticular file :-> python -m pytest test_demo1.py -m login
#To generate html report need to install one package - pip install pytest-html
# run command  python -m pytest test_google_test.py -v --html=google_report.html
