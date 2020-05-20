FROM python:3.8.3-alpine

LABEL maintainer="Soramon0" version="1.0"

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirement.txt requirement.txt

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r requirement.txt && apk del .tmp-build-deps

COPY ./app /app

RUN adduser -D user
USER user