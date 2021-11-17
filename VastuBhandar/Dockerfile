FROM python:3.8.10

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app


COPY requirements.txt ./
COPY . .

RUN pip3 install --no-deps -r requirements.txt
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
