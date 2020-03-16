# We will use the ubuntu image as the base
FROM ubuntu

# update apt-get, install apt-utils
RUN apt-get update \
    && apt-get install -y --no-install-recommends apt-utils
    
# set up node stuff
RUN apt-get install -y curl \
    && curl -sL https://deb.nodesource.com/setup_12.x | bash - \
    && apt-get install -y nodejs
    
# set up python stuff
RUN apt-get -y install python3 \
    && apt-get -y install python3-venv \
    && apt-get -y install python3-venv python3-pip \
    && pip3 install piazza-api

# copy app files from repo to local volume
ADD ./ /home/node/app

RUN cd /home/node/app \
    && npm install \
    && npm run