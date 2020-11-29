from python:3.9-alpine

expose 8000

workdir /app

add . /app

run apk add --update musl-dev gcc libffi-dev
run apk add postgresql-dev
run apk add build-base
run pip install -r requirement.txt

cmd uvicorn server:app --reload --host 0.0.0.0