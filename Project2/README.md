# Project 2 Documentation
### Name: Hunter Seitz

## Part 1
![VPC](https://i.imgur.com/UgZLJ56.png)
Creating a VPC is simple where you can create an IP address with a CIDR notation with it. I go ahead with 10.0.0.0/24. Below is the VPC is created. 
![VPC1](https://i.imgur.com/fgsf1fH.png)
Next, created the Subnet by using the /28 notation to correspond with the overall VPC IP. Below the first screenshot is where the Subnet is created. 
![Subnet](https://i.imgur.com/UgZLJ56.png)
![Subnet1](https://i.imgur.com/5JxPCMC.png)
![GW](https://i.imgur.com/SHwbSzR.png)
Second, created the gateway for the VPC as attached. 
![RT](https://i.imgur.com/LTpdVF4.png)
Third, created route tables to attach it with the VPC and dictates how packets are forwarded. 
![RT1](https://i.imgur.com/22MCRZ2.png)
![SG](https://i.imgur.com/9TS8ckF.png)
Lastly, security groups are created as firewall. Below is my inbound rules that allows SSH traffic specifically. 
![inbound](https://i.imgur.com/hCNbKqX.png)


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
![instance](https://i.imgur.com/NBMEcJ0.png)
While accessing from using ssh command and got into the AMI instance. 
![ssh](https://i.imgur.com/W0R7s0X.png)
To change the hostname of the AMI, I did sudo hostnamectl set-hostname command to 
![login](https://i.imgur.com/PHvZLpE.png)
