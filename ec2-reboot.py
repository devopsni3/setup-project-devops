#Requirement: Reboot EC2 instances us-east-1 region
#aws sdk for python
#pip install boto3

import boto3

response = client.reboot_instances(
    InstanceIds=[
        'string',
    ],
    DryRun=True|False
)