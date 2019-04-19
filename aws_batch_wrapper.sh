#!/usr/bin/env bash
set -x

tmp_dir=$(python -c 'import sys,uuid; sys.stdout.write(uuid.uuid4().hex)')
src_s3=$1
src_local_path=$2/${tmp_dir}
dest_s3=$3
dest_local_path=$4/${tmp_dir}
minJava=$5
maxJava=$6
setupfile_s3=$7

mkdir -p ${src_local_path}
mkdir -p ${dest_local_path}

# install aws s3
pip3 install awscli

# Copy data from s3
aws s3 cp ${src_s3} ${src_local_path}

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
aws aws s3 cp --recursive ${dest_local_path} ${dest_s3}