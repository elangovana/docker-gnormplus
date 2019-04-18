FROM lanax/gnormplus@sha256:fa5e104802bcfedbba49f2e836b141b24930f8a3cbba6ca8b35f268b033f3aea
MAINTAINER Elangovan


RUN add-apt-repository ppa:jonathonf/python-3.5
RUN apt-get update
RUN apt-get install python3.5 -y
RUN apt-get install python3-pip -y


ADD aws_batch_wrapper.sh /GNormPlusJava

WORKDIR /GNormPlusJava
CMD ["/bin/bash"]