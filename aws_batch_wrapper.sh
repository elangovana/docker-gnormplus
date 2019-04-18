#!/usr/bin/env bash

src_s3=@1
src_local_path=@2
dest_s3=@3
dest_local_path=@4
minJava=@5
maxJava=@6
setupfile_s3=@7

mkdir -p ${src_local_path}
mkdir -p ${dest_local_path}

# install aws s3
pip3 install awscli

# Copy data from s3
aws s3 sync ${src_s3} ${src_local_path}
# Optionally copy setup s3
if [ "${setupfile_s3}" = "" ]; then
    echo "No set up file.. Using default"
else
    echo using ${setupfile_s3}
    aws s3 cp ${setupfile_s3} /GNormPlusJava/setup.txt
fi

# Run
cd /GNormPlusJava
java -Xmx${maxJava} -Xms${minJava} -jar GNormPlus.jar ${src_local_path}  ${dest_local_path} setup.txt

# Copy results back s3
aws s3 sync ${dest_local_path} ${src_local_path}