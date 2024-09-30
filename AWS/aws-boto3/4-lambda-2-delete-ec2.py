# Boto3 = Gives the ability to manage AWS services using python

import boto3

def terminate_instance(ID):
    # goto_ec2_page = boto3.client('ec2', access_key_id='AK, secret_access_key='SK', region_name='us-east-1')
    
    goto_ec2_page = boto3.client('ec2')
    response = goto_ec2_page.terminate_instances(InstanceIds=ID)
    print(f"Terminating instance with ID: {ID}") 
    
    # print(response)

# Entry Point of the code
def lambda_handler(event, context):
    instances_list = [
           'i-0c309eb8b4399f87b',
           'i-0f5bda584b8336038'
        ]
         
    terminate_instance(instances_list)