FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /book_rentals

COPY requirements.txt /book_rentals/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /book_rentals/

