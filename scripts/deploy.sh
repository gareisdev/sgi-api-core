#!/bin/bash

# VARIABLES
path_dc_file=../docker-compose.yaml

## Update project
git pull

## Run docker 
docker-compose -f $path_dc_file build
docker-compose -f $path_dc_file up -d 
