FROM python:2.7-jessie
MAINTAINER Santiago Basulto <santiago@rmotr.com>

# Supress warnings about missing front-end. As recommended at:
# http://stackoverflow.com/questions/22466255/is-it-possibe-to-answer-dialog-questions-when-installing-under-docker
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y apt-file && \
    apt-file update && \
    apt-get install -y vim unzip openssh-client

WORKDIR /app
ADD . /app

RUN mkdir /root/.jupyter && cp jupyter_notebook_config.py /root/.jupyter

RUN pip install --no-cache-dir -U setuptools

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN rm -f Dockerfile requirements.txt jupyter_notebook_config.py
