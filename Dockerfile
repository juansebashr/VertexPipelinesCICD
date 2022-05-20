FROM python:3.9

WORKDIR /POC
ADD . /POC

RUN pip install -r requirements.txt
