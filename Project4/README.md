### Name: Hunter Seitz

# Project 4 

The config file in ssh sets the host name of the instance by adding the private IP
associated with the name of the instance. 
The proxy and the webserv1 instances are in different subnets, but in a
same bane of the cloud. To ssh into the webserv1 instance, we can 
`ssh -i (key) ubuntu@webserv1`. The webserv1 at the end is the hostname I set in by
the ssh config file. 

- Setting up HAProxy 
    - Setting up
        - The HAProxy is stored in the /etc directory and we can edit the haproxy.cfg file to set any configurations like maxconn (maximum number of connections) or log (warnings).
        - Configurations
            - The Frontend should be the accessing the proxy in that case, the HAProxy. 
                - frontend (proxy ip)
                - bind the private IP of the instance
                - default backend references web_servers
            - The Backend references the webserv1 instance and runs on it. 
                - balance roundrobin
                - the private IP of the webserv1 and webserv2
        - `sudo systemctl restart haproxy.service`
        - resources
            - [Installing on Ubuntu](https://www.haproxy.com/blog/how-to-install-haproxy-on-ubuntu/)
            - [Introduction to HAProxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
            - [Four Essentials](https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/)
- Webserver 
    - I used Apache2 for this instance. 
    - Setting up
        - The index HTML files. 
        - There are no configurations are made. 
        - The site HTML files are stored in /var/www/html because the apache2 can read the files from the www directory where it finds HTML files. 
        - `sudo systemctl restart apache2.service`
        - Resources 
            - [Installing Apache2](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04) 
            
- Connecting to proxy and two webservers.  
![webserv1](https://github.com/WSU-kduncan/ceg3120-hunter2seitz/blob/main/Project4/images/webserv1.png)
![webserv2](https://github.com/WSU-kduncan/ceg3120-hunter2seitz/blob/main/Project4/images/webserv2.png) 
