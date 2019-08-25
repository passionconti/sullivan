FROM ubuntu:18.04
FROM python:3.7

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN pip3 install pipenv

RUN mkdir /app

WORKDIR /app

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --deploy --system

COPY . /app

CMD flask run
