FROM python:3.8.5-slim

LABEL author="andyi95"
LABEL maintainer="Andrey Chernikov"
LABEL release-date="2021-07-04"

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r /code/requirements.txt

# Накатили слой с установленными pip пакетами, после чего можно копировать
# всё остальное
COPY . .

CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000
