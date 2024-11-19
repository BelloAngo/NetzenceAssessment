import logging

from botocore.exceptions import ClientError

from core.dependencies import get_s3_client
from core.settings import get_settings

# Globals
settings = get_settings()
s3_client = get_s3_client()


def upload_file_to_bucket(file_obj, folder, object_name=None):
    """Upload a file to an S3 bucket

    :param file_obj: File to upload
    :param folder: Folder to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_obj

    # Upload the file
    try:
        s3_client.upload_file(
            file_obj, settings.A_ARCHIVE_BUCKET, f"{folder}/{object_name}.json"
        )
    except ClientError as e:
        logging.error(e)
        return False
    return True
