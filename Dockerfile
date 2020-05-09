FROM python:3.8-slim

COPY /requirements.txt /opt/requirements.txt
WORKDIR /opt
RUN pip3 install -r ./requirements.txt
