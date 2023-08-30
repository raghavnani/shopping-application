### 1. Get python image
FROM python:3.7-buster

RUN apt-get update -y && \
    apt-get upgrade -y


### 2. Install Python
COPY requirements.txt /src/
WORKDIR /src


RUN pip install -r requirements.txt

COPY app /src/app
COPY config /src/config
COPY run.py /src




ENV FLASK_ENV=development
EXPOSE 4000

# enable waiting for db
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait
