FROM ubuntu:16.04
MAINTAINER Santiago Basulto <santiago@rmotr.com>

# Supress warnings about missing front-end. As recommended at:
# http://stackoverflow.com/questions/22466255/is-it-possibe-to-answer-dialog-questions-when-installing-under-docker
ARG DEBIAN_FRONTEND=noninteractive

# Essentials: developer tools, build tools, OpenBLAS
RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-utils git curl vim unzip openssh-client wget \
    build-essential cmake \
    libopenblas-dev software-properties-common

RUN add-apt-repository -y ppa:deadsnakes/ppa && apt-get update
RUN apt-get install -y  --no-install-recommends python3.6 python3.6-dev python3-pip && \
    pip3 install --no-cache-dir --upgrade pip setuptools && \
    echo "alias python='python3'" >> /root/.bash_aliases && \
    echo "alias pip='pip3'" >> /root/.bash_aliases

RUN apt-get install -y --no-install-recommends libjpeg-dev zlib1g-dev

RUN apt-get install -y --no-install-recommends \
    libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev \
    libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libgtk2.0-dev \
    liblapacke-dev checkinstall

RUN rm -f /usr/bin/python3 /usr/bin/python3m /usr/bin/pip /usr/local/bin/pip /usr/local/bin/pip3
RUN ln -s /usr/bin/python3.6 /usr/bin/python3
RUN ln -s /usr/bin/python3.6m /usr/bin/python3m
RUN ln -s /usr/bin/pip3 /usr/bin/pip

WORKDIR /app
ADD . /app

RUN mkdir /root/.jupyter && cp jupyter_notebook_config.py /root/.jupyter

RUN pip install --no-cache-dir -U setuptools

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN rm -f Dockerfile requirements.txt jupyter_notebook_config.py
