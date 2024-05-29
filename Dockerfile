FROM python:3.10-slim-buster
WORKDIR /app

COPY ./setup.py .

RUN python3 -m ensurepip
RUN pip install .
