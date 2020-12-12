FROM python:3.8-alpine

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install packages
RUN apk update \
  && apk add gcc musl-dev libffi-dev openssl-dev postgresql-dev g++ \
  && apk add python3-dev zeromq-dev nodejs npm

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements /usr/src/app/requirements
RUN pip install -r requirements/develop.txt

# install jupyter frontend extension
RUN jupyter labextension install @krassowski/jupyterlab-lsp \
  && jupyter labextension install @ryantam626/jupyterlab_code_formatter \
  && jupyter serverextension enable --py jupyterlab_code_formatter

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/deployment/entrypoint.sh"]
