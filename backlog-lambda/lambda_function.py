import json
import boto3
from load_function import load_to_database

# Create SQS client
sqs = boto3.client('sqs')

def lambda_handler(event, context):
    print('lambda_handler: starting')

    # DLQ URL - replace with your actual DLQ URL
    dlq_url = 'https://sqs.eu-west-1.amazonaws.com/339713081862/CC-DLQ'  
    
    while True:
        # Receive message from DLQ
        response = sqs.receive_message(
            QueueUrl=dlq_url,
            MaxNumberOfMessages=10,  # Number of messages to fetch
            WaitTimeSeconds=0
        )
        
        messages = response.get('Messages', [])
        if not messages:
            print('No messages in DLQ')
            break

        for message in messages:
            try:
                # Process message
                print(f'Processing message: {message["Body"]}')
                # Assuming message body is JSON
                msg_body = json.loads(message['Body'])
                load_to_database([msg_body])  # Process the message
                print('Message loaded to database successfully')

                # Delete message from DLQ after successful processing
                sqs.delete_message(
                    QueueUrl=dlq_url,
                    ReceiptHandle=message['ReceiptHandle']
                )
                print('Message deleted from DLQ')

            except Exception as e:
                print(f'Error processing message: {e}')
                # Optionally handle re-queuing or other error handling
                pass

    return {
        'statusCode': 200,
        'body': json.dumps('DLQ messages processed successfully!')
    }
