# //////////////////////////////
# // Mitro Emailer
################################

FROM ubuntu:trusty
MAINTAINER Chris Roemmich <croemmich@myriadmobile.com>

# //////////////////////////////
# // Base
################################

RUN \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install python python-dev python-virtualenv python-pip libpq-dev

# //////////////////////////////
# // Mitro-Emailer
################################

RUN mkdir /data
COPY . /data
RUN \
    chmod 755 /data/*.sh && \
    cd /data && \
    rm -rf build && \
    sh build.sh

# //////////////////////////////
# // Clean
################################

# remove unneeded packages
RUN apt-get clean && apt-get autoremove -y

# clean temp directories
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# //////////////////////////////
# // Execute
################################

# set work dir
WORKDIR /data

# start mitro-emailer
CMD ["/data/docker-start.sh"]