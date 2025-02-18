#!/bin/zsh

# list all available locations.
az account list-locations -o table

# list all resource groups available
az group list -o table

# create storage account in the default location
az storage account create -n mdwinter1234 -g DataAcademyWinter2025

# create storage account in the uksouth region
az storage account create -n mdwinter1234 -g DataAcademyWinter2025 -l uksouth

# same as the above with the full parameters names
az storage account create --name mdwinter1234 --resource-group DataAcademyWinter2025 --location uksouth

# list all accounts
az storage account list -g DataAcademyWinter2025 -o table

# show storage account metadata
az storage account show --resource-group '<resource-group-name>' --name '<storage-account-name>'
az storage account show --resource-group '<resource-group-name>' --name '<storage-account-name>' --query id

# delete the mdwinter1234 account
az storage account delete -g DataAcademyWinter2025 -n mdwinter1234

# show the connection string to the account
az storage account show-connection-string -n mdwinter1234 -g DataAcademyWinter2025
az storage account show-connection-string --query connectionString -n mdwinter1234 -g DataAcademyWinter2025
az storage account show-connection-string --query connectionString --name mdwinter1234 --resource-group DataAcademyWinter2025

# list all the containers for an account
az storage container list --account-name mdwinter1234 --connection-string "<connectionString>" -o table

# delete a container
az storage container delete --name blobcontainer --account-name mdwinter1234 --connection-string "<connectionString>"
