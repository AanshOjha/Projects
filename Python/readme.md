# AWS Cloud Cost Optimization - Identifying Stale Resources

## 1. Delete/stop Unwanted Ec2 Instances 
In this example, we'll create a Lambda function that auto identifies all ec2 instances in a given region and then deletes them to save on compute, storage cost. 

### For trying it Yourself:
- [Lambda Code to delete all ec2 here]()


## Ec2 scheduler using lambda
Use Lambda to stop and start Amazon EC2 instances at regular intervals. This automatically stop and start my Amazon Elastic Compute Cloud (Amazon EC2) instances to reduce my Amazon EC2 usage.

- [Follow Tutorial here](https://repost.aws/knowledge-center/start-stop-lambda-eventbridge)

## 3. Identifying Stale EBS Snapshots

In this example, we'll create a Lambda function that identifies EBS snapshots that are no longer associated with any active EC2 instance and deletes them to save on storage costs.

### Description:

The Lambda function fetches all EBS snapshots owned by the same account ('self') and also retrieves a list of active EC2 instances (running and stopped). For each snapshot, it checks if the associated volume (if exists) is not associated with any active instance. If it finds a stale snapshot, it deletes it, effectively optimizing storage costs.

### For trying it Yourself:

- [Lambda Code Here](./delete_stale_ebs.py)
- For testing: 
1. create ec2 and volumes snapshot
2. delete ec2
3. test lambda notice it auto deletes snapshot :) 