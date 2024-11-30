def view_all_books(library):
    if library!=[]:
        for book in library:
            print("\n*Book Details: ")
            print(f"Title: {book['title']}\nAuthor Name: {book['authorN']}\nID NO: {book['Isbn']}\nPrice: {book['price']}\nQuantity: {book['quantity']}")
            print()
    else:
        print("No books available in the library")
        print()

        