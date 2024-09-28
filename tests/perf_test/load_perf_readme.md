

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


### run in root folder 
```cmd
python -m locust
```
- this will start the performance test

- then click open localhost:8089 in the browser

