FROM python:3.9

WORKDIR /code

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --dev --system

COPY ./app /code/app
COPY main.py main.py

EXPOSE 8000

CMD uvicorn main:_app --host 0.0.0.0 --port 8000
