FROM python:3.6-jessie
MAINTAINER Santiago Basulto <santiago@rmotr.com>

# Supress warnings about missing front-end. As recommended at:
# http://stackoverflow.com/questions/22466255/is-it-possibe-to-answer-dialog-questions-when-installing-under-docker
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y apt-file && \
    apt-file update && \
    apt-get install -y vim unzip openssh-client curl

WORKDIR /app
ADD . /app

RUN mkdir /root/.jupyter && cp jupyter_notebook_config.py /root/.jupyter

RUN pip install --no-cache-dir -U setuptools

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && nvm install stable"
RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter labextension install @oriolmirosa/jupyterlab_materialdarker"

RUN pip install jupyterlab-git flake8

RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter labextension install jupyterlab_bokeh"
RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter labextension install @jupyterlab/git"
RUN jupyter serverextension enable --py jupyterlab_git

RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter labextension install @mflevine/jupyterlab_html"
RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter labextension install jupyterlab-flake8"
RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter labextension install @ijmbarr/jupyterlab_spellchecker"
RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter labextension install @jupyterlab/xkcd-extension"

RUN echo "echo 'Happy hacking ;)'" >> /root/.bashrc

RUN rm -f Dockerfile requirements.txt jupyter_notebook_config.py
