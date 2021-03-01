# pull official base image
FROM python:3.9-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 0

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get install -y libpq-dev gcc libpangocairo-1.0-0 fonts-deva


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# remove build dependencies
RUN apt-get autoremove -y gcc


# copy project
COPY . .