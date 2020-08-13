FROM python:3.8-alpine

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
  && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev openssl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements /usr/src/app
RUN pip install -r requirements/develop.txt

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/deployment/entrypoint.sh"]
