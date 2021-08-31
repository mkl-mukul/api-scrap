FROM python:3

WORKDIR /app


run pip install --upgrade pip
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

RUN python manage.py migrate
