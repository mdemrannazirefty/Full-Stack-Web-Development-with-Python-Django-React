def update_book(library):
    if library is None or not library: 
        print("The library is empty. No book to update.")
        return library

    updatebook = int(input("Enter Book ID to Update: "))
    for book in library:
        if book['Isbn'] == updatebook:  
            print("\nBook Found")
            print("Current Book Details:")
            print(f"Title: {book['title']}")
            print(f"Author Name: {book['authorN']}")
            print(f"ID NO: {book['Isbn']}")
            print(f"Price: {book['price']}")
            print(f"Quantity: {book['quantity']}")
            
            book['title'] = input("Enter New Title: ") or book['title']
            book['authorN'] = input("Enter New Author Name: ") or book['authorN']
            book['price'] = float(input("Enter New Price: ") or book['price'])
            book['quantity'] = int(input("Enter New Quantity: ") or book['quantity'])

            print("Book Updated")
            return library

    print("Book Not Found")
    return library
