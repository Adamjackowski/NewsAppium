Automated tests
========================

## Instructions for starting automated tests 

### 1 - General requirements:

1. Appium must be installed. It can be the newest version.
2. Python3 must be added to the PATH environment path.
3. PyTest must be installed. It can be the newest version.
4. The config.json file must be added to the project -> See "Storing login details".
5. After each failed test, the screenshot of last viewed screen is saved in /screenshots folder.

### 2 - For the VS Code program:

1. Download the "Python" extension. Open the project folder.
2. To run a given test, in the explorer (upper left corner) discover the tests, select the test file of interest, press PPM and select the option to run tests from a given file.
3. To run each method you can open a test file and choose run/debug button above each test method.

### 3 - To be run in the console

1. Open the console window in the project folder (Ctrl + Shift + RightMouseButton -> open console window).
2. To run all tests use the pytest command in the root direcory. The test will be executed on default browser - Firefox -> See "Run on different browsers".
```
pytest
```
3. To run the selected test, use the command pytest filename with Tests_py.
```
pytest test_name.py
```

### 5 - Test scructure

1. Tests are written in "Page Object Pattern" - please get familiar with it before starting to implement new ones.
2. Each test is in each file and each file contain each test methods. Each method contain each test data and setUp and tearDown fuctions -> see next points.
3. Some setUp and a little bit of test data is put into a fixtures in conftest.py file. Be aware to not change the scope of each and keep names of each params unique. See -> https://docs.pytest.org/en/latest/fixture.html.

##  Storage of login details 

### 1 - The config.json file

1. Config file json should be in the tests/ folder.
2. The config.json file should contain the following fields (values must be completed with valid data).

```
{
    "existing_login": "",
    "existing_password": "",
    "not_existing_login": "",
    "not_existing_password":""
}

  }
```