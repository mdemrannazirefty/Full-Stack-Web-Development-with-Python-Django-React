from Save_Books import Save_Books
from datetime import datetime

def update_book(library):
    if not library:
        print("The library is empty. No book to update.")
        return library

    updatebook = input("Enter Book Title to Update: ")
    
    for book in library:
        if book['Title'] == updatebook:  
            print("\nBook Found")
            print("Current Book Details:")
            print("---------------------------------------------")
            print(f"Title: {book['Title']}")
            print(f"Author Name: {book['Author']}")
            print(f"ID NO: {book['Isbn']}")
            print(f"Published Year: {book['Year']}")
            print(f"Price: {book['Price']}")
            print(f"Quantity: {book['Quantity']}")
            print("---------------------------------------------")
            book_last_updated_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            book['Authorn'] = input("Enter New Author Name: ") or book['Author']
            book['Year'] = input("Enter New Published Year: ") or book['Year']
            book['Price'] = float(input("Enter New Price: ") or book['Price'])
            book['Quantity'] = int(input("Enter New Quantity: ") or book['Quantity'])
            book["bookLastUpdatedAt"] = book_last_updated_at
            

            Save_Books(library)
            print("Book Updated")
            print()
            return library

    print("Book Not Found")
    return library
