# Transform - Remove sensitive data
import csv

transaction_list = []
with open("leeds_09-05-2023_09-00-00.csv", "r+") as transact_info_file: # LOAD customer information from the file
    transactions = csv.DictReader(transact_info_file, fieldnames=["Date and time", "Location", "Customer", "Item(s)", "Total price", "Payment method", "Card number"], delimiter=',')

    # for transaction in transactions:
    #     # print(transaction)
    #     del(transaction[6]) # could do delete 2, then delete 5
    #     del(transaction[2])
    #     transaction_list.append(transaction)
    #     # print(transaction)
    # for transaction in transaction_list:
    #     print(transaction)

    with open("Sensitive-removed.csv", "w") as result:
        writer = csv.writer(result)

        writer.writerow(["Date and time", "Location", "Item(s)", "Total price", "Payment method"])

        for t in transactions:
            writer.writerow((t["Date and time"], t["Location"], t["Item(s)"], t["Total price"], t["Payment method"]))
            # writer.writerow((t[0:2], t[3:6]))
        
        # result.close()
        
        
    
    # transactions = transact_info_file.readlines()
    # for transaction in transactions:
        
    # for transaction in transactions:
    #     # transaction_list.append(transaction.rstrip()) #this one doesn't leave spaces between each customer
    #     transaction_list.append(transaction) #this one does leave a blank line between each customer
    # # print(transaction_list)
    # for transaction in transaction_list:
    #     print(transaction)
    # for transaction in transaction_list:


# import csv
# # opens a CSV file, reads its contents into a dictionary
# def load_csv_to_dict(file):
#     data_list = []
#     with open (file, mode='r') as csvfile:
#         reader = csv.DictReader(csvfile, fieldnames=['DateTime',' Location', 'Customer', 'Items', 'Total', 'PaymentMethod', 'CardNumber'])
#         for row in reader:
#             data_list.append(row)
         
#     return data_list
 
# # defines a variable file with the path to the CSV file to be loaded
# file = 'leeds_09-05-2023_09-00-00.csv'
# # calls the load_csv_to_dict function with the specified file and stores the returned dictionary in the variable data.
# data = load_csv_to_dict(file)
# for row in data:
#     print(row)