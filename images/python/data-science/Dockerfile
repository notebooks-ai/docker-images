FROM notebooksai/base-python-3.8:v1
MAINTAINER Team Notebooks AI <team@notebooks.ai>

# Supress warnings about missing front-end. As recommended at:
# http://stackoverflow.com/questions/22466255/is-it-possibe-to-answer-dialog-questions-when-installing-under-docker
ARG DEBIAN_FRONTEND=noninteractive

ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

RUN rm -f requirements.txt

# Extra lab extensions
RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter labextension install @jupyter-widgets/jupyterlab-manager@1.1 --no-build"
RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter labextension install @bokeh/jupyter_bokeh@1.1.1 --no-build"
RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter labextension install jupyterlab-plotly@1.5.1 --no-build"
RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter labextension install plotlywidget@1.5.1 --no-build"
RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter labextension install jupyterlab-dash@0.1.0-alpha.3 --no-build"

RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && jupyter lab build"


