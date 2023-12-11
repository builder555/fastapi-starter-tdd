# FastAPI primer

This [FastAPI](https://fastapi.tiangolo.com) starter template provides a simple and efficient way to begin a new web project, including preconfigured setup for test-driven development (TDD).

## Features:

* unit/e2e and mutation testing
* CORS preconfigured
* sample allowed-origins
* example routing in submodule
* black code formatter

## Usage

### Requirements

* python3
* pipenv

### Install

```shell
git clone https://github.com/builder555/fastapi-starter-tdd
cd fastapi-starter-tdd
pipenv install --dev
```

### Run tests
```shell
# unit/e2e test
pipenv run test

# app/tests/test_main.py .
# app/tests/test_module.py .


# mutation test
pipenv run mutation
# 1. Running tests without mutations
# ⠋ Running...Done
#
# 2. Checking mutants
# ⠹ 21/21  🎉 12  ⏰ 0  🤔 0  🙁 9  🔇 0

# see results
pipenv run mutresult
```

### Start a dev server

```shell
pipenv run start:dev
```

Navigate to http://localhost:8000/docs to see the Swagger UI or http://localhost:8000/redoc to see ReDoc.

To monitor tests while developing, run

```shell
pipenv run testmon
```

## Structure

```bash
├── app #<-- all your modules live here
│   ├── __init__.py
│   ├── module.py #<-- example module
│   └── tests #<-- unit/integration tests are here. these files are excluded from mutation
│       ├── __init__.py
│       ├── test_main.py
│       └── test_module.py
└── main.py #<-- main application code
```

## Running in a Docker container

```
docker build -t fastapi:latest . && docker run --rm -d -p 8000:8000 fastapi:latest
```

Navigate to http://localhost:8000/docs to see the Swagger UI or http://localhost:8000/redoc to see ReDoc.
