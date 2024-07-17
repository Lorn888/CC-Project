import csv

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