from Save_Books import Save_Books

def remove_book(library):
    if not library:
        print("No books available to remove.")
        return library
    
    removebook = input("Enter Book Title : ")
    for book in library:
        if book["Title"] == removebook:
            library.remove(book)
            Save_Books(library)
            print("Book has been removed.")
            print()
            return library
        
    
    print("Book not found in the library.")
    print()
    return library