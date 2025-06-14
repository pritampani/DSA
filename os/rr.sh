#!/bin/bash

# Prompt the user for their username and password
read -p "Enter username: " username
read -sp "Enter password: " password
echo

# Predefined username and password
valid_username="root"
valid_password="confidential"

# Check if the entered username and password match the predefined values
if [ "$username" == "$valid_username" ] && [ "$password" == "$valid_password" ]; then
    echo "Valid user"
else
    echo "Not a valid user"
fi
