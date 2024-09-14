# CI/CD Pipeline School-Project

## Table of Contents

1. [TOC](#toc)
2. [Resources](#resources)
3. [Installation](#installation)


## Resources
A collection of useful links for further reading and reference:
- [Python argparse Documentation](https://docs.python.org/3/library/argparse.html)
- [Python Logging Documentation](https://docs.python.org/3/library/logging.html#logrecord-attributes)
- [Python os Documentation](https://docs.python.org/3/library/os.html)

## Installation
To install the required dependencies for this project, run the following command:


**The sets up the pip enabled**
```cmd
python -m pip install --upgrade pip
```

**This command installs all the Python packages and dependencies listed in the requirements.txt file located in the BE (Back-End) directory.**
```cmd
pip install -r BE/requirements.txt
```
- for more information on assertpy, chekout [assertpy documentation](https://pypi.org/project/assertpy/#description)

**Check the current version of asssertpy**
´´´cmd
pip show assertpy
´´´

**To install the openapi python client**
´´´cmd
pip install openapi-python-client
´´´

**To install the API client folder**
´´´cmd
python -m openapi_python_client generate --url http://localhost:5000/openapi.json
´´´





## Tests

### Unittesting

**This command is for running the pytest on the machine**
```cmd
python -m pytest --maxfail=1 --exitfirst --strict-markers
```
- **`python`**: This invokes the Python interpreter. It ensures that the command is executed using the correct Python environment, which is especially important when working with virtual environments.

- **`-m`**: This flag tells Python to run a module as a script. The module name follows the `-m` flag. In this case, `pytest` is the module being executed.

- **`pytest`**: `pytest` is a powerful testing framework for Python that makes it easy to write simple and scalable test cases. Running this module discovers and executes the tests in your project, and then provides a detailed report of the results.

- **`--maxfail=1`**: This option instructs `pytest` to stop running tests after the first test failure is encountered. This is useful in CI/CD pipelines because it allows the pipeline to fail quickly, providing immediate feedback on critical issues and saving resources by not running the entire test suite when a problem is detected early.

- **`--exitfirst`**: This option complements `--maxfail=1` by immediately exiting after the first test failure, further ensuring that the pipeline fails fast. This can be particularly helpful when the goal is to address the first failing test before moving on to the rest.

- **`--strict-markers`**: This option enforces strict handling of custom markers in your test suite. If a marker is used in your tests but is not registered in your `pytest` configuration (e.g., `pytest.ini` or `conftest.py`), `pytest` will raise an error. This helps maintain consistency and prevents typos or misconfigurations from slipping through in the CI/CD pipeline.



**Code Coverage**
´´´´cmd
python -m pytest --cov
´´´
- **`--code-coverage`**: the other one way with "pytest" as start does not work for my machine and as a windows 10 and above user i recommend using this.

### Integration testing

**API start**
´´´´cmd
python BE/calculator.py --rest
´´´


 