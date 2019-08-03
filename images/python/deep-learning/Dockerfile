FROM notebooksai/data-science-python:v1
MAINTAINER Team Notebooks AI <team@notebooks.ai>

# Supress warnings about missing front-end. As recommended at:
# http://stackoverflow.com/questions/22466255/is-it-possibe-to-answer-dialog-questions-when-installing-under-docker
ARG DEBIAN_FRONTEND=noninteractive

ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

RUN rm -f requirements.txt

EXPOSE 8888 6006
