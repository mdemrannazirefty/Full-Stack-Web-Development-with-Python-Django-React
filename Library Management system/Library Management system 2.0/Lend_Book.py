import json
from datetime import datetime, timedelta
from Save_Books import Save_Books

def lend_book(library):
    if not library:
        print("The library is empty.")
        print()
        return library

    title = input("Enter the Book Title to Lend: ").strip()
    for book in library:
        if book["Title"].strip().lower() == title.lower():
            if book["Quantity"] > 0:
                borrower_name = input("Enter Your Name: ").strip()
                phone_number = input("Enter Your Phone Number: ").strip()  # Keep it as a string

                # Optional: Validate that the phone number contains only digits
                if not phone_number.isdigit():
                    print("Invalid phone number. Please enter digits only.")
                    print()
                    return library
                due_date = (datetime.now() + timedelta(days=30)).strftime("%d-%m-%Y")

                book["Quantity"] -= 1
                Save_Books(library)

                lend_info = {
                    "Title": book["Title"],
                    "Borrower": borrower_name,
                    "Phone": phone_number,
                    "DueDate": due_date
                }

                try:
                    with open("lendData.json", "r") as file:
                        lend_data = json.load(file)
                except FileNotFoundError:
                    lend_data = []

                lend_data.append(lend_info)
                with open("lendData.json", "w") as file:
                    json.dump(lend_data, file, indent=4)

                print(f"Book {book['Title']} lent successfully")
                print()
                return library
            else:
                print("Not available to lend.")
                print()
                return library

    print("Book not found in the library.")
    print()
    return library
