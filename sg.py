import boto3
ec2 = boto3.resource('ec2')
sg = ec2.SecurityGroup('sg-0a26445216499acb2')
rules = sg.ip_permissions
#print (sg.group_name)
#print (rules)
for rule in rules:
#    print (rule['IpRanges'])
    for sourcerange in rule['IpRanges']:
#        print (sourcerange['CidrIp'])
        if sourcerange['CidrIp']  == '0.0.0.0/0':
            sg.revoke_ingress(IpPermissions=[rule])
            print ("Deleted: Security Group ID: {} Rule: {}".format(sg.group_id, rule))
        else:
            print ("Rules are as per standerds")
