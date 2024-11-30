def remove_book(library):
    if library is None or not library:  
        print("The library is empty. No book to remove.")
        return library

    removebook = int(input("Enter Book ID: "))
    for book in library:
        if book['Isbn'] == removebook:  
            library.remove(book)
            print("Book Removed")
            print()
            return library

    print("Book Not Found") 
    print()
    return library
