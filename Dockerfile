FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY ./src/requirements.txt /app
RUN pip install -r /app/requirements.txt

COPY ./src/ /app
