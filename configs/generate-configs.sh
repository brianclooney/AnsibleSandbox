#!/bin/bash

# Function to generate a random password
generate_password() {
  tr -dc A-Za-z0-9 </dev/urandom | head -c 20 ; echo ''
}

# Read the template
config=$(cat $1)

# Generate secrets
JWT_SECRET=$(generate_password)
DB_ROOT_PASSWORD=$(generate_password)
DB_PASSWORD=$(generate_password)
RABBITMQ_PASSWORD=$(generate_password)

# Replace placeholders
config=$(echo "$config" | sed "s/{{JWT_SECRET}}/$JWT_SECRET/g")
config=$(echo "$config" | sed "s/{{DB_ROOT_PASSWORD}}/$DB_ROOT_PASSWORD/g")
config=$(echo "$config" | sed "s/{{DB_PASSWORD}}/$DB_PASSWORD/g")
config=$(echo "$config" | sed "s/{{RABBITMQ_PASSWORD}}/$RABBITMQ_PASSWORD/g")

# Save to final config file
mkdir -p out
echo "$config" > out/$1
