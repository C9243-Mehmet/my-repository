# AWS ProjectsAWSTemplateFormatVersion: 2010-09-09
Description: This template launches an EC2 with a security group that enables SSH
  
Parameters: 
  
Resources:
LogicalID:
  Type: AWS::EC2::Instance
  Properties:
    ImageId: "ami-02e136e904f3da870"
    InstanceInitiatedShutdownBehavior: "String"
    InstanceType: "t2.micro"
    Ipv6AddressCount: Number
    Ipv6Addresses:
      Ipv6Addresses
    KernelId: "String"
    KeyName: "myfirstSSHkeypair"
    LaunchTemplate:
      LaunchTemplateId: "String"
      LaunchTemplateName: "String"
      Version: "String"
    LicenseSpecifications:
      LicenseSpecifications
    Monitoring: String
    NetworkInterfaces:
      NetworkInterfaces
    PlacementGroupName: "String"
    PrivateIpAddress: "String"
    RamdiskId: "String"
    SecurityGroupIds:
      sg-00e21936a0368613d
    SourceDestCheck: false
    SsmAssociations:
      SsmAssociations
    SubnetId: "String"
    Tags:
      -
        Key: Name
        Value: MyTag 
    Tenancy: "String"
    UserData:
        Fn::Base64: !Sub |
          #!/bin/bash -xe
          sudo yum update -y
          sudo yum install httpd -y
          sudo /etc/init.d/httpd start
          wget 
    Volumes:
      Volumes
  
Outputs: