import psycopg2
from connection_db import get_db_connection

def load_to_database(cleaned_data):
    # Ensure cleaned_data is a list of records
    if isinstance(cleaned_data, dict):
        cleaned_data = [cleaned_data]

    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        for row in cleaned_data:
            # Check if a transaction with the same details already exists
            cursor.execute("""
                SELECT transaction_details_id FROM transactions_details
                WHERE timestamp = %s AND location = %s AND total_amount = %s AND payment_method = %s
            """, (
                row['Time Stamp'],
                row['Location'],
                row['Total Amount'],
                row['Payment Method']
            ))
            existing_transaction = cursor.fetchone()

            if existing_transaction:
                print(f"Duplicate transaction found: {row}. Skipping.")
                continue

            # Insert into transactions_details table
            cursor.execute("""
                INSERT INTO transactions_details (timestamp, location, total_amount, payment_method)
                VALUES (%s, %s, %s, %s)
            """, (
                row['Time Stamp'],
                row['Location'],
                row['Total Amount'],
                row['Payment Method']
            ))

            # Retrieve the inserted transaction_details_id
            cursor.execute("""
                SELECT MAX(transaction_details_id) FROM transactions_details
            """)
            transaction_details_id = cursor.fetchone()[0]

            # Insert items into the items table and transactions table
            for item in row['Item(s)']:
                item_name = item['name']
                item_price = item['price']

                # Insert or retrieve item_id from items table
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
                    """, (item_name, item_price))

                    # Retrieve the inserted item_id
                    cursor.execute("""
                        SELECT MAX(item_id) FROM items
                    """)
                    item_id = cursor.fetchone()[0]

                # Insert into transactions table
                cursor.execute("""
                    INSERT INTO transactions (item_id, transaction_details_id)
                    VALUES (%s, %s)
                """, (item_id, transaction_details_id))

        connection.commit()
        print('Data loaded into database successfully')
    except Exception as e:
        print(f'Failed to load data into database: {e}')
        connection.rollback()
        raise e
    finally:
        cursor.close()
        connection.close()
