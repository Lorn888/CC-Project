import csv
import boto3

def extract_csv_from_s3(bucket_name, filename, download_path):
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, filename, download_path)
        print(f"File {filename} downloaded successfully to {download_path}.")
    except Exception as e:
        print(f"Error downloading file from S3: {e}")

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
