### Name: Hunter Seitz

# Project 5

### Part 1

- Installed the Docker for the WSL2 by downloading the Windows application
of Docker and let it install. With WSL2 option is enabled. 
- To build a container, we can pull an image from the Docker Hub:
    - `docker pull image`
- To run the container:
    - `docker run -it image`
- To view the project, we can access the page by from `localhost` and with port 80 to display
contents from a http file. 
### Part 2
- To create a DockerHub public repo, click on click repository button and do all necessary configurations such as changing visibility so its on public by default. Then, create. 
- The credentials needed for GitHub Secrets are the DockerHub token and the username associated with it. Such ass USERNAME, PASSWORD, and TOKEN.
- The GitHub workflow is used by a template and changed variables such as repository name. 
- The GitHub workflow works by reading from the file and do jobs by running actions and scripts each time. Environment variables can be changed by name, jobs, etc. 

### Part 3
- Container restart script is a script that let you to restart one or more containers.
- Webhook task definition file is a file that has tasks as variables to execute events or jobs within the deployment. 
- Setting up webhook
    - I created the listener by using the command; `webhook -hooks path/to/webhook-config.json -verbose`  
    - Installing the webhook by `sudo apt install webhook` and run it by `path/to/webhook -hooks hooks.json -verbose` 
- To set up a notifier in GitHub, you can configure in the webhook as a function by requiring hostname and the port. 

### Result
![image](https://github.com/WSU-kduncan/ceg3120-hunter2seitz/blob/main/Project5/website1.png)


