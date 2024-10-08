# CI/CD Pipeline School-Project

## Table of Contents

1. [Resources](#resources)
2. [Installation](#installation)
3. [Docker](#Docker-Issues)


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
```cmd
pip show assertpy
```

**To install the openapi python client**
```cmd
pip install openapi-python-client
```

**To install the API client folder**
```cmd
python -m openapi_python_client generate --url http://localhost:5000/openapi.json
```





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

´´´cmd
python -m pytest --cov
´´´

- **`--code-coverage`**: the other one way with "pytest" as start does not work for my machine and as a windows 10 and above user i recommend using this.

### Integration testing

**API start**

´´´cmd
python BE/calculator.py --rest
´´´


### END 2 END Test

- perhaps add something important here 




 ## Docker 


 ### Docker Issues

 **docker is not running**
 - if you get an issue in the terminal when running any docker command that looks like this:

 ```cmd
 ERROR: error during connect: Head "http://%2F%2F.%2Fpipe%2FdockerDesktopLinuxEngine/_ping": open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.¨
 ```
 - then you probably need to run docker on your desktop, (right-click the logo on if you can find it in the windows bar and hit 'restart')


### commands (chronologic order)

**in order to run the docker container you have to set up selenium in docker**
```cmd
docker run --name selenium -d --add-host host.docker.internal:host-gateway -p 4444:4444 -p 5900:5900 --shm-size="2g" selenium/standalone-chrome:4.2.1-20220531
```

**in order to run the docker container with the two images (FE DF & BE DF through the docker-compose.yml file in the root folder)**
```cmd
docker compose -p webcalculator up -d  
```
- the command will run the docker container, if u run it with the "-d" you will run the container in the background which allows you to execute commands after runner the command above

**now you can run the test**
```cmd
python -m pytest -s -v
```
or
```cmd
pytest -s -v
```
or if you are on mac
```cmd
python3 -m pytest -s -v
```