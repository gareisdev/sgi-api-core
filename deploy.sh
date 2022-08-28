#!/bin/bash

## Update project
git pull

## Run docker 
docker-compose build
docker-compose up -d


