import psycopg2
import boto3
import json
import os

ssm_client = boto3.client('ssm')

def get_ssm_param(param_name):
    """
    Retrieve the Redshift connection details from AWS SSM Parameter Store.
    """
    print(f'get_ssm_param: getting param_name={param_name}')
    parameter_details = ssm_client.get_parameter(Name=param_name, WithDecryption=True)
    redshift_details = json.loads(parameter_details['Parameter']['Value'])
    print(f'get_ssm_param loaded for db={redshift_details["database-name"]}, user={redshift_details["user"]}, host={redshift_details["host"]}')
    return redshift_details

def get_db_connection():
    """
    Establishes a connection to the Redshift database using the connection details from SSM Parameter Store.
    """
    ssm_param_name = os.environ.get('SSM_PARAMETER_NAME', 'NOT_SET')
    redshift_details = get_ssm_param(ssm_param_name)

    connection = psycopg2.connect(
        host=redshift_details['host'],
        database=redshift_details['database-name'],
        user=redshift_details['user'],
        password=redshift_details['password'],
        port=redshift_details['port']
    )
    return connection
