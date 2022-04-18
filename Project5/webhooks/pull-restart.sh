#!/bin/bash


docker kill sample-website
yes | docker system prune

docker pull wsuseitz47/ceg3120work:latest

docker run -d --rm --name sample-website -p 80:80 wsuseitz47/ceg3120work:latest