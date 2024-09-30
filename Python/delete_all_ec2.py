'''
AUTHOR: AJ

AIM: TO STOP ALL RUNNING EC2's IN GIVEN REGION

MODIFICATION: TO MAKE THE SCRIPT DELETE ALL EC2's JUST REPLACE THE WORD "stop" WITH "delete"
EVERYWHERE :) 

'''

import boto3 

############ Set region
REGION = 'ap-south-1'

# THIS SCRIPT RETURNS ID of RUNNING Ec2 Instances 

def running_ec2(REGION):
    # connect to ec2 service of that region
    ec2 = boto3.client('ec2', region_name=REGION)

    # All Running instances 
    response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        },
    ]
    )

# Extract ID of Instnaces
# beacuse the response is in the Dict Reservations so,
    ID = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            ID.append(instance['InstanceId'])
    return ID

def ec2_stop(EC2_2_Stop):
    ec2 = boto3.client('ec2', region_name=REGION)
    ec2.stop_instances(
    InstanceIds=EC2_2_Stop)

    print('*'*50)
    print(f'Stopped Your Ec2 with ID: {EC2_2_Stop}')
    print('*'*50)

def lambda_handler(event, context):
    print(running_ec2(REGION))
    EC2_2_Stop = running_ec2(REGION)
    ec2_stop(EC2_2_Stop)