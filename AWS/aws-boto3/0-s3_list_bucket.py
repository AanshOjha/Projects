'''
IAM Setup = https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration

AWS Recommends = Use an Integrated Development Environment (IDE) like VS code etc
which supports the AWS Toolkit enabling authentication through IAM Identity Center

response  = <class 'dict'>

'''

#######################
# This Prints all buckets in your AWS Account
#######################

import boto3

def list_buckets():
    # connect to s3 
    client = boto3.client('s3')
# save response
    response = client.list_buckets()
# print high level keys
    print(list(response.keys()))

# this gives list of buckets
    print(response['Buckets'])

    # invalid = TypeError: list indices must be integers or slices, not str
    # print(response['Buckets']['Name'])

 # GET NAME OF BUCKETS
    for bucket in response['Buckets']:
        print(bucket['Name'])

    # print(type(response),response,sep="\n")

# run the function: 
list_buckets()





