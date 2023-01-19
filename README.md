# FastAPI primer

## Usage

### Install

```shell
git clone https://github.com/builder555/fastapi-starter-tdd
cd fastapi-starter-tdd
pipenv install --dev
```

### Run tests
```shell
# unit test
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
