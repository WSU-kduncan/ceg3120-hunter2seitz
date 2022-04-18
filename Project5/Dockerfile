docker run -dit -p 80:80 /home/hunterseitz/ceg3120/docker:/usr/local/apache2/htdocks/ httpd:2.4

FROM httpd:latest

RUN apt install -y python3

COPY html/ /usr/local/apache2/htdocs/index.html 

EXPOSE 80
