# coding: utf-8
import boto3
session = boto3.Session(profile_name='KevinPortfolioAdmin')
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='KevinVideolyzerVideosACloudGuru', CreateBucketConfiguration={'LocationConstraint': session.region_name})
bucket = s3.create_bucket(Bucket='KevinVideolyzerVideosACloudGuru421413321', CreateBucketConfiguration={'LocationConstraint': session.region_name})
bucket = s3.create_bucket(Bucket='KevinVideolyzerVideosACloudGuru421413321', CreateBucketConfiguration={'LocationConstraint': session.region_name})
session.region_name
bucket = s3.create_bucket(Bucket='ktptranvideolyzervideos', CreateBucketConfiguration={'LocationConstraint': session.region_name})
from pathlib import Path
get_ipython().run_line_magic('ls', '/Downloads/*.mp4')
get_ipython().run_line_magic('ls', 'Users/')
get_ipython().run_line_magic('ls', 'Desktop')
get_ipython().run_line_magic('ls', '~/Desktop')
get_ipython().run_line_magic('ls', '~/Downloads/*.mp4')
pathname = '~/Downloads/Pexels Videos 2539559.mp4'
path = Path(pathname).expenduser().resolve()
path = Path(pathname).expanduser().resolve()
print(path)
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object': {'Bucket': bucket.name, 'Name': path.name}})
response
job_id = resonse['JobId']
job_id = response['JobId']
result = rekognition_client.get_label_detection(JobId=job_id)
result
result.keys()
result['JobStatus']
result['ResponseMetadata']
result['VideoMetadata']
