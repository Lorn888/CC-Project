import json
from load_function import load_to_database

def lambda_handler(event, context):
    print('lambda_handler: starting')
    
    for record in event['Records']:
        message = json.loads(record['body'])
        print(f'Processing message: {message}')
        
        try:
            # Load the data into the database
            load_to_database(message)
            print('Message loaded to database successfully')
        except Exception as e:
            print(f'Error loading message to database: {e}')
            raise e
    
    return {
        'statusCode': 200,
        'body': json.dumps('Messages processed successfully!')
    }
