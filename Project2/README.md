# Project 2 Documentation
### Name: Hunter Seitz

## Part 1
![VPC](https://i.imgur.com/UgZLJ56.png)
Creating a VPC is simple where you can create an IP address with a CIDR notation with it. I go ahead with 10.0.0.0/24. Below is the VPC is created. 
![VPC1](/Images/VPC1.png)
Next, created the Subnet by using the /28 notation to correspond with the overall VPC IP. Below the first screenshot is where the Subnet is created. 
![Subnet](/Images/Subnet.png)
![Subnet1](/Images/Subnet1.png)
![GW](/Images/gateway1.png)
Second, created the gateway for the VPC as attached. 
![RT](/Images/route table.png)
Third, created route tables to attach it with the VPC and dictates how packets are forwarded. 
![RT1](/Images/route table1.png)
![SG](/Images/securitygroups.png)
Lastly, security groups are created as firewall. Below is my inbound rules that allows SSH traffic specifically. 
![inbound](/Images/InboundRules.png)


## Part 2 
On creating a new AMI instance, I attach the my VPC using the Network section 
and the same for Subnet. The default username of the instance is ec2-user. 
From using Public IPv4 address, you can enable it. If we disabled it, there's no 
IPv4 address associated with the instance even Elastic one. 
Then, attaching the volume to the instance should be a root volume already made.
You can add another storage option though. 
To reserve an Elastic IP address, we can allocate an Elastic IP address and then click
on Actions and go to Associate Elastic IP address. There's the instance type and associate
it with the VPC. 
![instance](/Images/instance.png)
While accessing from using ssh command and got into the AMI instance. 
![ssh](/Images/ssh access.png)
To change the hostname of the AMI, I did sudo hostnamectl set-hostname command to 
![login](/Images/hostnamelogin.png)
