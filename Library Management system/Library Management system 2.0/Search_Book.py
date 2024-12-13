def search_book(library):
    if library is None or not library:
        print("The library is empty.")
        return library

    searchbook = input("Enter Book Title: ")
    for book in library:
        if book['Title'] == searchbook:  
            print("\nBook Found")
            print("---------------------------------------------")
            print("*Book Details:")
            print(f"Title: {book['Title']}")
            print(f"Author Name: {book['Author']}")
            print(f"ID NO: {book['Isbn']}")
            print(f"Publisher Year: {book['Year']}")
            print(f"Price: {book['Price']}")
            print(f"Quantity: {book['Quantity']}")
            print("---------------------------------------------")
            print()
            return library
    print("Book Not Found")
    print()
    return library
