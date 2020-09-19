FROM notebooksai/data-science-python:v3
MAINTAINER Team Notebooks AI <team@notebooks.ai>

# Supress warnings about missing front-end. As recommended at:
# http://stackoverflow.com/questions/22466255/is-it-possibe-to-answer-dialog-questions-when-installing-under-docker
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y clustalo mafft

ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

RUN rm -f requirements.txt

# Extra lab extensions
RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter labextension install @jupyterlab/fasta-extension --no-build"
RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build"
RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter labextension install nglview-js-widgets@2.6.9 --no-build"

RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter lab build --dev-build=False --minimize=False"

RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && JUPYTER_TOKEN=None jupyter nbextension enable --py nglview"
RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && JUPYTER_TOKEN=None jupyter nbextension enable --py widgetsnbextension"