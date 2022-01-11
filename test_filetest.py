import pytest
import os

def test01_pytest_selftest():
    print("Pytest is now running")
    assert True
    
def test02_testfile_output():
    assert "This is a test file" in os.system('python testfile.py').stdout()
     
    