import json
import os
import psutil
import time
from dotenv import load_dotenv
# pip install azure-identity
from azure.identity import DefaultAzureCredential
# pip install azure-storage-blob
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Load the .env file
load_dotenv()

try:
    print("Hello, Azure Blob Storage!")
    account_url = "https://mdwinter1234.blob.core.windows.net"
    # this method is recommended, but requires proper role configuration and role assignment
    # default_credential = DefaultAzureCredential()
    # Create the BlobServiceClient object
    # blob_service_client = BlobServiceClient(account_url=account_url, credential=default_credential)
    # or use connection string (not recommended)
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    container_name = str(time.strftime("%Y-%m-%d"))

    # ! TODO create container, or if we get an exception get container client
    try:
        container_client = None  # TODO
    except Exception as ex:
        container_client = None  # TODO
        print("Exception: ")
        print(ex)

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

    # TODO Create a blob client using the local file name as the name for the blob
    blob_client = None  # TODO
    print("\nUploading to Azure Storage:\n\t" + local_file_name)
    # TODO Upload the created file
    with open(file=upload_file_path, mode="rb") as data:
        None  # TODO

    print("\nListing json files...")

    # TODO List the blobs in the container
    blob_list = None  # TODO
    for blob in blob_list:
        print("\t" + blob.name)

    # TODO From the list of all blobs download the blob we just created
    blob_list = None  # TODO
    for blob in blob_list:
        if blob.name == local_file_name:
            download_file_path = os.path.join(local_path, str.replace(local_file_name, '.json', '_DOWNLOAD.json'))
            print("\nDownloading files \n\t" + download_file_path)
            with open(file=download_file_path, mode="wb") as download_file:
                None  # TODO

    # if you don't need anymore, or want to start over, you can delete the whole container
    # print("\nDeleting container...")
    # TODO delete the container

except Exception as ex:
    print("Exception: ")
    print(ex)
