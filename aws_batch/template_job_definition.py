def get_job_definition(account, region, container_name, job_def_name, job_param_s3uri_destination, memoryInMB, ncpus,
                       role_name):
    """
This is the job definition for this sample job.
    :param account:
    :param region:
    :param container_name:
    :param job_def_name:
    :param memoryInMB:
    :param ncpus:
    :param role_name:
    :return:
    """
    return {
        "jobDefinitionName": job_def_name,
        "type": "container",
        # These are the arguments for the job
        "parameters": {
            "src_local": "/data/input",
            "dest_local": "/data/output",
            "src_s3": job_param_s3uri_destination,
            "dest_s3":job_param_s3uri_destination,
            "minMemory":"10G",
            "maxMemory": "20G",
            "s3_setup_file":job_param_s3uri_destination


        },
        # Specify container & jobs properties include entry point and job args that are referred to in parameters
        "containerProperties": {
            "image": container_name,
            "vcpus": ncpus,
            "memory": memoryInMB,
            "command": [
                "/bin/bash",
                "aws_batch_wrapper.sh",
                "Ref::src_s3",
                "Ref::src_local",
                "Ref::dest_s3",
                "Ref::dest_local",
                "Ref::minMemory",
                "Ref::maxMemory",
                "Ref::s3_setup_file"
            ],
            "jobRoleArn": "arn:aws:iam::{}:role/{}".format(account, role_name),
            "volumes": [
                {
                    "host": {
                        "sourcePath": job_def_name
                    },
                    "name": "data"
                }
            ],
            "environment": [
                {
                    "name": "AWS_DEFAULT_REGION",
                    "value": region
                }
            ],
            "mountPoints": [
                {
                    "containerPath": "/data",
                    "readOnly": False,
                    "sourceVolume": "data"
                }
            ],
            "readonlyRootFilesystem": False,
            "privileged": True,
            "ulimits": [],
            "user": ""
        },
        "retryStrategy": {
            "attempts": 5
        }
    }
