FROM rmotr/base-python-3.6:v3
MAINTAINER Santiago Basulto <santiago@rmotr.com>

# Supress warnings about missing front-end. As recommended at:
# http://stackoverflow.com/questions/22466255/is-it-possibe-to-answer-dialog-questions-when-installing-under-docker
ARG DEBIAN_FRONTEND=noninteractive

ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

RUN rm -f requirements.txt

# Extra lab extensions
RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter labextension install jupyterlab_bokeh"
RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter labextension install @jupyterlab/plotly-extension"
