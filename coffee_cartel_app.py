import csv


def load_csv_to_dict(file):
    data_list = []
    try:
        with open(file, mode="r") as csvfile:
            reader = csv.DictReader(
                csvfile,
                fieldnames=[
                    "Time Stamp",
                    " Location",
                    "Customer",
                    "Item(s)",
                    "Total Amount",
                    "Payment Method",
                    "Card Number",
                ],
            )
            # reading field and converting it to a list of dictionaries
            for row in reader:
                # Items field of each row is split into individual items using split(', ')
                items = row["Item(s)"].split(", ")
                items_dict = []
                for item in items:
                    # Each item is further split into name and price using rsplit(' - ', 1). This ensures that any hyphens in the item names do not interfere with the splitting process.
                    name, price = item.rsplit(" - ", 1)
                    # strip any leading/trailing whitespace and convert the price to a float.
                    items_dict.append({name.strip(): float(price.strip())})
                    row["Item(s)"] = items_dict
                    data_list.append(row)
    except FileNotFoundError:
        print(f"The file {file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return data_list


# defines a variable file with the path to the CSV file to be loaded
file = "leeds_09-05-2023_09-00-00.csv"
# calls the load_csv_to_dict function with the specified file and stores the returned dictionary in the variable data.
data = load_csv_to_dict(file)


# Transform - Remove sensitive data
with open(
    "leeds_09-05-2023_09-00-00.csv", "r"
) as transact_info_file:  # LOAD customer information from the file
    transactions = csv.DictReader(
        transact_info_file,
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

    # writing the cleaned data set into "Sensitive-removed.csv" and if file didnt previously exist it creates one
    with open("Sensitive-removed.csv", "w") as result:
        writer = csv.writer(result)
        # setting the header for the csv file
        writer.writerow(
            ["Time Stamp", "Location", "Item(s)", "Total Amount", "Payment Method"]
        )  #
        for transaction in transactions:
            writer.writerow(
                (
                    transaction["Time Stamp"],
                    transaction["Location"],
                    transaction["Item(s)"],
                    transaction["Total Amount"],
                    transaction["Payment Method"],
                )
            )
