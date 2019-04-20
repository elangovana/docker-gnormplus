import argparse
import logging
from time import sleep

import boto3
import sys


def submit_job(job_def, queue_name, src_s3, dest_s3, s3_setup, src_local="/data/input", dest_local="/data/output",
               min_mem="10G", max_mem="20G"):
    client = boto3.client('batch')
    response = client.submit_job(
        jobName='gnormplus_new',
        jobQueue=queue_name,
        jobDefinition=job_def,
        parameters={
            "src_local": src_local,
            "dest_local": dest_local,
            "src_s3": src_s3,
            "dest_s3": dest_s3,
            "minMemory": min_mem,
            "maxMemory": max_mem,
            "s3_setup_file": s3_setup

        },
        timeout={
            'attemptDurationSeconds': 86400 * 2
        }
    )

    print(response)


def get_bucketname_key(uripath):
    assert uripath.startswith("s3://")

    path_without_scheme = uripath[5:]
    bucket_end_index = path_without_scheme.find("/")

    bucket_name = path_without_scheme
    key = "/"
    if bucket_end_index > -1:
        bucket_name = path_without_scheme[0:bucket_end_index]
        key = path_without_scheme[bucket_end_index + 1:]

    return bucket_name, key


def list_files(s3path_prefix):
    assert s3path_prefix.startswith("s3://")
    assert s3path_prefix.endswith("/")

    bucket, key = get_bucketname_key(s3path_prefix)

    s3 = boto3.resource('s3')

    bucket = s3.Bucket(name=bucket)

    return ((o.bucket_name, o.key) for o in bucket.objects.filter(Prefix=key))


def submit_multiple(job_def, queue_name, s3_source_prefix, s3_destination_prefix, s3_setup,
                    src_local="/data/input", dest_local="/data/output",
                    min_mem="10G", max_mem="20G"):
    # Submit job for each prefix
    for s3_bucket, s3_key in list_files(s3_source_prefix):
        sleep(1)
        submit_job(job_def, queue_name, "s3://{}/{}".format(s3_bucket, s3_key), s3_destination_prefix,
                   s3_setup, src_local, dest_local,
                   min_mem, max_mem)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)],
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger = logging.getLogger(__name__)

    parser.add_argument("job_name",
                        help="Batch Job def name, e.g gnormplus:11")

    parser.add_argument("queue",
                        help="The name of the job queue", default="gnormplus")

    parser.add_argument("s3_source_prefix",
                        help="The s3 uri prefix that will contain the input/output data. e.g s3://mybucket/aws-batch-sample-python/")

    parser.add_argument("s3_dest_prefix",
                        help="The s3 uri prefix that will contain the input/output data. e.g s3://mybucket/aws-batch-sample-python/")

    parser.add_argument("s3_setup",
                        help="The s3 path for the setup file")

    args = parser.parse_args()

    # Register job
    submit_multiple(args.job_name, args.queue, args.s3_source_prefix, args.s3_dest_prefix, args.s3_setup)
    logger.info("Completed")
