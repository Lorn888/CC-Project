import json
import os
import boto3
from extract_function import extract_csv_from_s3, load_csv_to_dict
from transform_function import write_cleaned_csv
from load_function import load_to_database
from connection_db import get_db_connection

def create_tables():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        with open('schema_definition.sql', 'r') as file:
            sql_script = file.read()

        cursor.execute(sql_script)
        connection.commit()

        print('Tables created successfully in Redshift.')
    except Exception as e:
        print(f'Error creating tables: {e}')
        raise e
    finally:
        cursor.close()
        connection.close()

def lambda_handler(event, context):
    print('lambda_handler: starting')

    create_tables()

    ssm_param_name = os.environ.get('SSM_PARAMETER_NAME', 'NOT_SET')
    print(f'SSM_PARAMETER_NAME: {ssm_param_name}')
    if ssm_param_name == 'NOT_SET':
        return {
            'statusCode': 500,
            'body': json.dumps('SSM_PARAMETER_NAME environment variable not set')
        }

    # Extract bucket and filename from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    filename = event['Records'][0]['s3']['object']['key']
    download_path = '/tmp/' + filename

    # Ensure all intermediate directories exist
    local_dir = os.path.dirname(download_path)
    os.makedirs(local_dir, exist_ok=True)

    print(f'Downloading {filename} from bucket {bucket} to {download_path}')
    extract_csv_from_s3(bucket, filename, download_path)
    print(f'File {filename} downloaded successfully to {download_path}')
    
    print('Loading CSV data into dictionary')
    data = load_csv_to_dict(download_path)
    print('CSV data loaded into dictionary')
    
    output_file_name = "Sensitive-removed.csv"
    output_path = '/tmp/' + output_file_name
    
    # print(f'Cleaning data and writing to {output_path}')
    # cleaned_data = write_cleaned_csv(data, output_path)
    # print(f'Cleaned data written to {output_path}')

    print('Loading cleaned data to database')
    load_to_database(data)
    print('Cleaned data loaded to database')

    # cleaned_file_content = json.dumps(cleaned_data)
    # cleaned_file_name = "Sensitive-removed.csv"
    # print(f'Uploading cleaned data to S3 bucket {bucket} with filename {cleaned_file_name}')
    # s3 = boto3.client('s3')
    # s3.put_object(Bucket=bucket, Key=cleaned_file_name, Body=cleaned_file_content)
    # print('Cleaned data uploaded to S3')

    return {
        'statusCode': 200,
        'body': json.dumps('Data cleaned and uploaded successfully!')
    }
