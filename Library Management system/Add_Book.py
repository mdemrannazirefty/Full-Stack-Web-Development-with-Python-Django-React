from Save_Books import Save_Books

def add_book(library):
    title = input("Enter Book Title: ")
    authorN = input("Enter Author Name: ")
    Isbn = int(input("Enter Book Id: "))
    price = float(input("Enter Book Price: "))
    quantity = int(input("Enter Quantity: "))
    
    book = {"title": title, "authorN": authorN, "Isbn": Isbn, "price": price, "quantity": quantity}
    if library is None:
        library = [] 
    
    library.append(book)
    Save_Books(library)
    print("Your Book Added Successfully")
    print()

    return library

   