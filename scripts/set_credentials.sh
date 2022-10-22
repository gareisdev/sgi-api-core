#!/bin/bash

# COLORS
NO_COLOR='\033[0m'
LIGHT_RED='\033[1;31m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
YELLOW='\033[1;33m'

# Get root path
root_path=$(git rev-parse --show-toplevel)


printf "${GREEN} ========== ${NO_COLOR}DB Config ${GREEN}==========\n"

printf "${YELLOW}[+]${NO_COLOR} DB NAME: "
read db_name

printf "${YELLOW}[+]${NO_COLOR} DB USER: "
read db_user

printf "${YELLOW}[+]${NO_COLOR} DB PASSWORD: "
read -s db_pass

printf "${GREEN} ========== ${NO_COLOR}DJANGO Config ${GREEN}==========\n"

printf "${ORANGE}[?]${NO_COLOR} Do you want generate a SECRET_KEY? (y/n): "
read create_secret_key

if [[ "$create_secret_key" == "y" || "$create_secret_key" == "Y" ]]; then
    secret_key=$(echo $RANDOM$RANDOM$RANDOM | base64 | rev | cut -c2- | rev)
    echo "$secret_key"
else
    printf "${YELLOW}[+]${NO_COLOR} SECRET KEY: "
    read -s secret_key
fi


printf "${ORANGE}[*]${NO_COLOR} Creating DB Config\n"

sed -i.bak "s/POSTGRES_DB.*/POSTGRES_DB=$db_name/g" "$root_path/env_files/DB.env"
sed -i.bak "s/POSTGRES_USER.*/POSTGRES_USER=$db_user/g" "$root_path/env_files/DB.env"
sed -i.bak "s/POSTGRES_PASSWORD.*/POSTGRES_PASSWORD=$db_pass/g" "$root_path/env_files/DB.env"


printf "${ORANGE}[*]${NO_COLOR} Creating DJANGO Config\n"

sed -i.bak "s/DB_NAME.*/DB_NAME=$db_name/g" "$root_path/env_files/DJANGO_CONFIG.env"
sed -i.bak "s/DB_USER.*/DB_USER=$db_user/g" "$root_path/env_files/DJANGO_CONFIG.env"
sed -i.bak "s/DB_PASSWORD.*/DB_PASSWORD=$db_pass/g" "$root_path/env_files/DJANGO_CONFIG.env"
sed -i.bak "s/DJANGO_SECRET_KEY.*/DJANGO_SECRET_KEY=$secret_key/g" "$root_path/env_files/DJANGO_CONFIG.env"
