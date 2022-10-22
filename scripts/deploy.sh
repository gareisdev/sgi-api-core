#!/bin/bash

# COLORS
NO_COLOR='\033[0m'
LIGHT_RED='\033[1;31m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
YELLOW='\033[1;33m'


# VARIABLES
root_path=$(git rev-parse --show-toplevel)
path_dc_file="${root_path}/docker-compose.yaml"

## Update project
printf "${GREEN}[+] Pulling from GitHub . . .\n"
git pull -q

# Get environment
printf "${ORANGE}[?] Environment (dev|prd): "
read environment

# Validate input
if [[ ! "$environment" =~ ^(dev|prd)$ ]]; then
    printf "${LIGHT_RED}[!] You need to indicate a valid environment (dev or prd)\n"
    exit 1
fi

# Set credentials
printf "${NO_COLOR} Config credentials"
bash "$root_path/scripts/set_credentials.sh"

# Create config to the project
printf "${GREEN}[+] Creating containers with configuration to environment: $environment\n"
sed -i.bak "s/DJANGO_SETTINGS_MODULE=.*/DJANGO_SETTINGS_MODULE=api_core.settings.$environment/g" "$root_path/env_files/DJANGO_CONFIG.env"

# Create requierements.txt with Poetry
printf "${GREEN}[+] Creating requirements.txt\n"
poetry export --without-hashes --format=requirements.txt > "$root_path/requirements.txt"

# Build Containers
printf "${GREEN}[+] Building containers . . . \n"
docker-compose -f $path_dc_file build -q

# Up containers
printf "${ORANGE}[?] You want up the containers? (Y/N): "
read up_containers

if [[ "$up_containers" == "y"  || "$up_containers" == "Y" ]]; then
    printf "${GREEN}[+] Starting containers\n"
    docker-compose -f $path_dc_file up -d
    printf "${GREEN}[+] Project up! See the ${NO_COLOR}logs${GREEN} to get more info\n"
else
    printf "${YELLOW}[*] Skipping start containers\n"
fi
