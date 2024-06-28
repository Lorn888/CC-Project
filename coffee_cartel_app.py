from db_connection import get_db_connection
import csv

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

def write_cleaned_csv(data, output_file):
    cleaned_data = []
    try:
        with open(output_file, "w", newline='') as result:
            writer = csv.writer(result)
            writer.writerow(["Time Stamp", "Location", "Item(s)", "Total Amount", "Payment Method"])
            for row in data:
                items_str = ", ".join([f"{item['name']} - {item['price']}" for item in row["Item(s)"]])
                writer.writerow([
                    row["Time Stamp"],
                    row["Location"],
                    items_str,
                    row["Total Amount"],
                    row["Payment Method"]
                ])
                cleaned_data.append({
                    "Time Stamp": row["Time Stamp"],
                    "Location": row["Location"],
                    "Item(s)": row["Item(s)"],
                    "Total Amount": row["Total Amount"],
                    "Payment Method": row["Payment Method"]
                })
        print(f"Cleaned data written to {output_file}")
    except FileNotFoundError:
        print(f"The file {output_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return cleaned_data

# Example usage:
input_file = "leeds_09-05-2023_09-00-00.csv"
output_file = "Sensitive-removed.csv"

data = load_csv_to_dict(input_file)
cleaned_data = write_cleaned_csv(data, output_file)


# Load cleaned data into the database
def load_to_database(data):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            for row in data:
                timestamp = row["Time Stamp"]
                location = row["Location"]
                total_amount = row["Total Amount"]
                payment_method = row["Payment Method"]

                cursor.execute("""
                    INSERT INTO transactions_details
                    (timestamp, location, total_amount, payment_method)
                    VALUES (%s, %s, %s, %s)
                    RETURNING transaction_details_id
                """, (timestamp, location, total_amount, payment_method))
                transaction_details_id = cursor.fetchone()[0]

                items = row["Item(s)"]
                for item in items:
                    item_name = item["name"]
                    item_price = item["price"]

                    cursor.execute("""
                        SELECT item_id FROM items WHERE item_name = %s AND item_price = %s
                    """, (item_name, item_price))
                    result = cursor.fetchone()
                    if result:
                        item_id = result[0]
                    else:
                        cursor.execute("""
                            INSERT INTO items (item_name, item_price)
                            VALUES (%s, %s)
                            RETURNING item_id
                        """, (item_name, item_price))
                        item_id = cursor.fetchone()[0]

                    cursor.execute("""
                        INSERT INTO transactions
                        (item_id, transaction_details_id)
                        VALUES (%s, %s)
                    """, (item_id, transaction_details_id))

            connection.commit()
            print("Data loaded into database")
    except Exception as e:
        print(e)
    finally:
        if connection:
            connection.close()

# Call load_to_database with the cleaned data
load_to_database(cleaned_data)
