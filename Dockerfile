# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app

USER daemon
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --user

COPY . .

ENV FLASK_APP=server.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
