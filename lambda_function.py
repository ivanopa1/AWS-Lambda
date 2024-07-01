import json
import boto3
import gzip
import os
import shutil

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    # Get the bucket and object key from the event
    #bucket = 's3-onboard-test'
    #key = 'mysql_fn1.gz'
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    if not key.endswith('.gz'):
        return
    
    # Download the .gz file from S3
    download_path = f'/tmp/{os.path.basename(key)}'
    s3.download_file(bucket, key, download_path)
    
    # Unarchive the .gz file
    with gzip.open(download_path, 'rb') as f_in:
        unarchived_file_path = f'/tmp/{os.path.basename(key)[:-3]}'
        with open(unarchived_file_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    
    # Upload the unarchived file back to the same bucket
    unarchived_key = key[:-3]
    s3.upload_file(unarchived_file_path, bucket, unarchived_key)
    
    # Delete the original .gz file
    s3.delete_object(Bucket=bucket, Key=key)
    
    return {
        'statusCode': 200,
        'body': f'Successfully processed {key}'
    }