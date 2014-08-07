# Python Dev environment
FROM orchardup/python:2.7
MAINTAINER <joe.weber.@vokalinteractive.com>
RUN apt-get update -qq && apt-get install -y python-psycopg2
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
