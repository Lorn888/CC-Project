import json
import boto3
from load_function import load_to_database

# Initialize the SQS and S3 clients
sqs = boto3.client('sqs')
dlq_url = 'https://sqs.eu-west-1.amazonaws.com/339713081862/CC-DLQ'

def process_messages_from_queue(queue_url):
    """Process messages from a given SQS queue."""
    print(f"Processing messages from queue: {queue_url}")
    messages = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10,  
        WaitTimeSeconds=20
    ).get('Messages', [])

    for message in messages:
        message_body = json.loads(message['Body'])
        print(f'Processing message: {message_body}')

        try:
            load_to_database([message_body])
            print('Message loaded to database successfully')
            # Delete the message from the queue once processed
            sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])
        except Exception as e:
            print(f'Error loading message to database: {e}')

def lambda_handler(event, context):
    print('lambda_handler: starting')

    # Process messages from the main queue
    if 'Records' in event:
        for record in event['Records']:
            message = json.loads(record['body'])
            print(f'Processing message: {message}')
            
            try:
                # Load the data into the database
                load_to_database([message])
                print('Message loaded to database successfully')
            except Exception as e:
                print(f'Error loading message to database: {e}')
                # Message will be retried by SQS or DLQ

    # After processing main queue, process messages from DLQ
    process_messages_from_queue(dlq_url)

    return {
        'statusCode': 200,
        'body': json.dumps('Messages processed successfully!')
    }
