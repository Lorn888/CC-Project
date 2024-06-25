import csv

def load_csv_to_dict(file):
    with open (file, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # Initialise the dictionary with keys from fieldnames and empty lists
        data_dict = {header: [] for header in reader.fieldnames}
        for row in reader:
            for header in reader.fieldnames:
                data_dict[header].append(row[header])

    return data_dict

file = 'leeds_09-05-2023_09-00-00.csv'
data = load_csv_to_dict(file)
print(data)

# def extract_data_from_csv(filename):
#     data = []
#     with open(filename, 'r', newline='') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             #These lines assign values from the row list to variables
#             timestamp = row[0]
#             customer = row[2]
#             items_ordered = row[3]
#             total_amount = float(row[4]) 
#             payment_method = row[5]
#             credit_card_number = row[6] 
            
#             # Split items ordered into a list
#             items_list = [item.strip() for item in items_ordered.split(',')]

#             # Prepare the extracted data
#             extracted_data = {
#                 'timestamp': timestamp,
#                 'customer': customer,
#                 'items_ordered': items_list,
#                 'total_amount': total_amount,
#                 'payment_method': payment_method,
#                 'credit_card_number': credit_card_number
#             }
#             data.append(extracted_data)
    
#     return data

# # Print the extracted data for verification
# for entry in extracted_data:
#     print(entry)

