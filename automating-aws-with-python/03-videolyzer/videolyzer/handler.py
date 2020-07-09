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
        })
    print(response)
    return


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
    print(event)
    return
