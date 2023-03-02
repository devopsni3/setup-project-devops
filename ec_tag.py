import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances(InstanceIds=[])
for instance in response['Reservations'][0]['Instances']:
    #print (instance['InstanceId'])
    #print (instance['Tags'])
    for tag_key in instance['Tags']:
        #print (tag_key['Value'])
        if tag_key['Key'] == 'Name1':
            print ("Application Tag is found for the EC2: {}".format(id))
        else:
            stop_response = ec2.stop_instances(InstanceIds=[id])
            print (stop_response)

#for i in response['Reservations']:
#    print (i)
#print (len(response['Reservations'][0]['Instances']))