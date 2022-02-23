FROM python:3.9.10-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /invoiceTest
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
