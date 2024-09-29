

# Performance Testing setup

## Install Locust


**i dont care if you are on mac, deal with it**

### command to install Locust
```cmd
pip install locust
```

## Steps To Run Locust te

**chronologic order**

### run in root folder 
```cmd
docker compose -f docker-compose-perf.yml up
```
- this will run the images in the container necessary for the use case


### run in root folder but in a seperate cli 
```cmd
python -m locust
```
- this will start the performance test

- then click open localhost:8089 in the browser (1)


- or, isntead of (1), yu can run the following command:


```cmd
python -m locust --host http://localhost:5000 --user 46 --spawn-rate 5 --autostart --headless --run-time 10s --only-summary --html report.html
```
1. `python -m locust` this will start the locust and it can be considered as main command 
```cmd
python -m locust
```

2. then you can add 'optional' command which if you don't add in the CLI will appear if you choose (1)
```cmd
--host http://localhost:5000
```
- this will specify the host you want to use 

3. this will specify how many users you want it to go up to as maximun and how many it'll increase with
```cmd
--user 46 --spawn-rate 5
```

4. adding this at the end of the command will start everything without needing to open the site in the browser
```cmd
--autostart --headless
```

5. this will merely specify a time-out when it should quit
```cmd
--run-time 10s
```

6. this will make sure that when you run it in the CLI you only receive the summary of the test
```cmd
--only-summary
```

7. this will report an html file as documentation on the test
```cmd
--html report.html
```

