import json

def view_all_lend():
    lend_data_file = "lendData.json"
    try:
        with open(lend_data_file, "r") as file:
            lend_data = json.load(file)

        if not lend_data:
            print("No lend records available.")
            print()
            return

        print()
        print("Lend and Return Details ")
        print("-------------------------------------------------")
        for index, record in enumerate(lend_data, start=1):
            print(f"Record {index}:")
            print(f"Title: {record['Title']}")
            print(f"Borrower: {record['Borrower']}")
            print(f"Phone: {record['Phone']}")
            print(f"Due Date: {record['DueDate']}")
            print("-----------------------------------------------")
        print()
    except FileNotFoundError:
        print("No lend or return records available.")
        print()