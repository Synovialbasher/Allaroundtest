import pytest
import pytest_console_scripts import ScriptRunner

def test01_pytest_selftest():
    print("Pytest is now running")
    assert True
    
def test02_testfile_output():
    ret = script_runner.run('testfile.py', print_result=True, shell=True)
    assert ret.success
    assert ret.stdout == "This is my test file!"