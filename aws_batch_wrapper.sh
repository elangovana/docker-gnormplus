#!/usr/bin/env bash

src_s3=@1
src_local_path=@2
dest_s3=@3
dest_local_path=@4
minJava=@5
maxJava=@6

mkdir -p ${src_local_path}
mkdir -p ${dest_local_path}

# install aws s3
RUN pip3 install awscli

# Copy from s3
aws s3 sync $(src_s3) ${src_local_path}

# Run
cd /GNormPlusJava
java -Xmx$(maxJava) -Xms$(minJava) -jar GNormPlus.jar ${src_local_path}  ${dest_local_path} setup.txt

# Copy results back s3
aws s3 sync $(dest_local_path) ${src_local_path}