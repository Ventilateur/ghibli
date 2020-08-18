# Ghibli movie list

## Requirements

## Solution
- Because we cannot call Ghibli API with each request, we need to have a cache system.
I decided to use Redis because of it's in-memory performance.  
- The data should not be older than one minute, so I decided to update the cache every 30 seconds with the data 
coming directly from Ghibli API. So I made a service that repeatedly queries Ghibli and update the cache.
- Finally, a minimal REST API service will query from Redis and return results to users.
- The reason to separate the public API and the data collector is to be able to scale them independently. 
When we have more traffics to the public API, we need more instances but we don't want to query Ghibli more frequently.
- The architecture is like below:  
**Ghibli API --> Data collector --> Redis --> Public API**

## How to run using docker compose
- Run ```make up``` which invokes ```docker-compose up -d --build``` and starts Redis, api and data collector.
- Head to [http://127.0.0.1:5000/movies](http://127.0.0.1:5000/movies) to see the results.
- You can also use ```127.0.0.1:5000/movies/<id>``` to query a particular film using its uuid.
- When done, run ```make down```.

## Configuration
- Configurations are done using environment variables, cf. services' config files for possible configurations.
- For [data collector](./data-collector), see [data-collector/config.py](./data-collector/config.py).
- For [public api](./api), see [api/config.py](./api/config.py).
- Change default configs in [docker-compose.yml](docker-compose.yml).

## To be improved
- Make end-to-end tests.
- Data collector is not distributed. I was thinking about using Celery for a distributed scheduler 
but it looks like an overkill for now.
- The config system needs a rework, the current one is cumbersome.
- Make redis persist data, in case Ghibli is down and redis restarts.
- Allow logs to be redirected to file.
- Make smaller images, maybe use python-slim.
