from Save_Books import Save_Books
import random
from datetime import datetime

def add_book(library):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    isbn = random.randint(1000, 9999)
    while True:
        try:
            year = int(input("Enter Published Year:"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    while True:
        try:
            price = float(input("Enter Book Price: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid Number.")       
    while True:
        try:
            quantity = int(input("Enter Quantity: "))
            break
        except ValueError:
            print("Invalid. Please enter a valid integer.")
    bookAddedAt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    book = {
        "Title": title, 
        "Author": author, 
        "Isbn": isbn,
        "Year":year,
        "Price": price, 
        "Quantity": quantity,
        "bookAddedAt": bookAddedAt,
        "bookLastUpdatedAt": ""
        }
    if library is None:
        library = [] 
    
    library.append(book)
    Save_Books(library)
    
    print("Your Book Added Successfully")
    print()
    return library

   