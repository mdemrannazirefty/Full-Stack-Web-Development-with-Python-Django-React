def search_book(library):
    if library is None or not library:  
        print("The library is empty.")
        return library

    searchbook = int(input("Enter Book ID: "))
    for book in library:
        if book['Isbn'] == searchbook:  
            print("\nBook Found")
            print("*Book Details:")
            print(f"Title: {book['title']}")
            print(f"Author Name: {book['authorN']}")
            print(f"ID NO: {book['Isbn']}")
            print(f"Price: {book['price']}")
            print(f"Quantity: {book['quantity']}")
            print()
            return library
        else:
            print("Book Not Found")
            return library