import json
import os
import boto3
import csv
from datetime import datetime
from extract_function import extract_csv_from_s3

sqs = boto3.client('sqs')

def convert_date_format(date_str):
    try:
        parsed_date = datetime.strptime(date_str, '%d/%m/%Y %H:%M')
        return parsed_date.strftime('%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        print(f"Error parsing date: {date_str}. Error: {e}")
        raise e

def load_csv_to_dict(file):
    data_list = []
    try:
        with open(file, mode="r") as csvfile:
            reader = csv.DictReader(
                csvfile,
                fieldnames=[
                    "Time Stamp",
                    "Location",
                    "Customer",
                    "Item(s)",
                    "Total Amount",
                    "Payment Method",
                    "Card Number",
                ],
            )
            for row in reader:
                # Convert date format
                row["Time Stamp"] = convert_date_format(row["Time Stamp"])
                
                items = row["Item(s)"].split(", ")
                items_dict = []
                for item in items:
                    name, price = item.rsplit(" - ", 1)
                    items_dict.append({"name": name.strip(), "price": float(price.strip())})
                row["Item(s)"] = items_dict
                data_list.append(row)
    except FileNotFoundError:
        print(f"The file {file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return data_list

def lambda_handler(event, context):
    print('lambda_handler: starting')

    # Extract bucket and filename from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    filename = event['Records'][0]['s3']['object']['key']
    download_path = '/tmp/' + os.path.basename(filename)

    print(f'Downloading {filename} from bucket {bucket} to {download_path}')
    extract_csv_from_s3(bucket, filename, download_path)
    print(f'File {filename} downloaded successfully to {download_path}')
    
    print('Loading CSV data into dictionary')
    data = load_csv_to_dict(download_path)
    print('CSV data loaded into dictionary')
    
    # Send the entire data list as a single message to SQS
    sqs_queue_url = os.environ['SQS_QUEUE_URL']
    response = sqs.send_message(
        QueueUrl=sqs_queue_url,
        MessageBody=json.dumps(data)
    )
    print(f'Message sent to SQS: {response["MessageId"]}')

    return {
        'statusCode': 200,
        'body': json.dumps('Data transformed and sent to SQS successfully!')
    }
