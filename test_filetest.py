import pytest
import subprocess



def test01_pytest_selftest():
    print("Pytest is now running")
    assert True
  
@pytest.mark.parametrize("file_name, file_text", [("testfile.py", "This is my test file!"),("additionalfile.py", "This is an additional python file.")])  
def test02_testfile_output(file_name, file_text):
    x = subprocess.run(('python ' + file_name), capture_output=True)
    output = str(x.stdout)
    assert str(file_text) in output
    
#def test03_additionalfile_output()

