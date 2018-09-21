FROM python:2.7-jessie
MAINTAINER Santiago Basulto <santiago@rmotr.com>

# Supress warnings about missing front-end. As recommended at:
# http://stackoverflow.com/questions/22466255/is-it-possibe-to-answer-dialog-questions-when-installing-under-docker
ARG DEBIAN_FRONTEND=noninteractive

RUN printf "\n\n" >> /etc/apt/sources.list
RUN echo '###### Debian Main Repos\n\
  deb http://deb.debian.org/debian/ oldstable main contrib non-free\n\
  deb-src http://deb.debian.org/debian/ oldstable main contrib non-free\n\
  deb http://deb.debian.org/debian/ oldstable-updates main contrib non-free\n\
  deb-src http://deb.debian.org/debian/ oldstable-updates main contrib non-free\n\
  deb http://deb.debian.org/debian-security oldstable/updates main\n\
  deb-src http://deb.debian.org/debian-security oldstable/updates main\n\
  deb http://ftp.debian.org/debian jessie-backports main\n\
  deb-src http://ftp.debian.org/debian jessie-backports main' >> /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y apt-file apt-utils && \
    apt-file update && \
    apt-get install -y vim unzip openssh-client curl texlive-xetex pandoc xzdec && \
    apt-get build-dep -y python-lxml

WORKDIR /app
ADD . /app

RUN pip install --no-cache-dir -U setuptools

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
RUN /bin/bash -c "source $HOME/.nvm/nvm.sh && nvm install stable"

RUN echo "printf 'Happy hacking ❤️ RMOTR Team'" >> /root/.bashrc
RUN echo "printf '\n\n'" >> /root/.bashrc

RUN echo "export PS1='\[\033[38;5;38m\]\[\033[0m\033[38;5;15m\]\u\[\033[0;36m\] @ \[\033[0;36m\]\h \n\[\033[0;32m\]└─\[\033[0m\033[0;32m\] \$\[\033[0m\033[0;32m\] ▶\[\033[0m\] '" >> /root/.bashrc

RUN rm -f Dockerfile requirements.txt
