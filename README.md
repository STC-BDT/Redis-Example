# Redis example with docker and python

## Run redis using docker compose

1. In the `docker` folder is available a docker compose witch run two services: `redis` and `redis-commander` ( a simple tool for exploring the resources in a redis database)

```bash
cd docker
```

2. Run the services using docker compose

```bash
docker compose up
```

## Run the python example

In the `src` folder an example f redis connection with python is available.

1. Install the requirements

```bash
pip install -r requirements.txt
```

2. move into the src directory

```bash
cd src
```

3. run the python file

```bash
python redis_with_python.py
```
