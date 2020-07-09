import json
import os
import urllib

import boto3

def start_label_detection(bucket, key):
    rekognition_client = boto3.client('rekognition')
    response = rekognition_client.start_label_detection(
        Video={
            'S3Object': {
                'Bucket': bucket,
                'Name': key
            }
        },
        NotificationChannel={
            'SNSTopicArn': os.environ['REKOGNITION_SNS_TOPIC_ARN'],
            'RoleArn': os.environ['REKOGNITION_ROLE_ARN']
        })
    print(response)
    return

def get_video_labels(job_id):
    pass

def put_labels_in_db(data, video_name, video_bucket):
    pass


# Lambda events

def start_processing_video(event, context):
    for record in event['Records']:
        start_label_detection(
            record[0]['s3']['bucket']['name'],
            urllib.parse.unquote_plus(record[0]['s3']['object']['key'])
        )

    print(response)
    # while not done:
    #   time.sleep(10)
    #   done = check_job_status()

    return


def handle_label_detection(event, context):
    for record in event['Records']:
        message = json.loads(record['Sns']['Message'])
        job_id = message['JobId']
        s3_object = message['Video']['S3ObjectName']
        s3_bucket = message['Video']['S3Bucket']

        response = get_video_labels(job_id)
        put_labels_in_db(response, s3_object, s3_bucket)
    return
