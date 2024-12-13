import json
from Save_Books import Save_Books

def return_book(library):
    if not library:
        print("The library is empty.")
        print()
        return library

    title = input("Enter the Book Title to Return: ").strip()
    for book in library:
        if book["Title"].strip().lower() == title.lower():
            try:
                with open("lendData.json", "r") as file:
                    lend_data = json.load(file)
            except FileNotFoundError:
                lend_data = []

            for lend in lend_data:
                if lend["Title"].strip().lower() == title.lower():
                    lend_data.remove(lend)
                    print(f"Book {title} returned successfully.")
                    book["Quantity"] += 1
                    Save_Books(library)

                    with open("lendData.json", "w") as file:
                        json.dump(lend_data, file, indent=4)
                    return library

            print("No lending found")
            print()
            return library

    print("Book not found in the library.")
    print()
    return library
