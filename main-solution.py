import json
import os
import psutil
import time
# pip install python-dotenv
from dotenv import load_dotenv
# pip install azure-identity
from azure.identity import DefaultAzureCredential
# pip install azure-storage-blob
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Load the .env file
load_dotenv()

try:
    print("Hello, Azure Blob Storage!")
    account_url = "https://mdtest4321.blob.core.windows.net"
    # this method is recommended, but requires proper role configuration and role assignment
    # default_credential = DefaultAzureCredential()
    # Create the BlobServiceClient object
    # blob_service_client = BlobServiceClient(account_url=account_url, credential=default_credential)
    # or use connection string (not recommended)
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    container_name = str(time.strftime("%Y-%m-%d"))

    # Get or create container
    container_client = blob_service_client.get_container_client(container_name)
    if not container_client.exists():
        container_client = blob_service_client.create_container(container_name)

    # Create a local directory to hold blob data
    local_path = "./data"
    isExist = os.path.exists(local_path)
    if not isExist:
        os.mkdir(local_path)

    # Create a file in the local data directory to upload and download
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    local_file_name = timestamp + ".json"
    upload_file_path = os.path.join(local_path, local_file_name)

    # Write text to the file
    file = open(file=upload_file_path, mode='w')

    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    data = {
        "timestamp": timestamp,
        "cpu_usage": cpu,
        "mem_usage": mem,
    }
    file.write(json.dumps(data, indent=4))
    file.close()

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    print("\nUploading to Azure Storage:\n\t" + local_file_name)
    # Upload the created file
    with open(file=upload_file_path, mode="rb") as data:
        blob_client.upload_blob(data)

    print("\nListing json files...")

    # List the blobs in the container
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print("\t" + blob.name)

    for blob in blob_list:
        if blob.name == local_file_name:
            download_file_path = os.path.join(local_path, str.replace(local_file_name, '.json', '_DOWNLOAD.json'))
            print("\nDownloading files \n\t" + download_file_path)
            with open(file=download_file_path, mode="wb") as download_file:
                download_file.write(container_client.download_blob(blob.name).readall())

    # if you don't need anymore, or want to start over, you can delete the whole container
    # print("\nDeleting container...")
    # container_client.delete_container()

except Exception as ex:
    print("Exception: ")
    print(ex)
