def view_all_books(library):
    print(f"\nLoaded {len(library)} Books from file.")
    print("---------------------------------------------")

    if library!=[]:
        for index, book in enumerate(library, start=1):
            print(f"*Book Details {index}: \nTitle: {book['Title']}\nAuthor Name: {book['Author']}\nID NO: {book['Isbn']}\nPublished Year:{book['Year']} \nPrice: {book['Price']}\nQuantity: {book['Quantity']}")
            print("---------------------------------------------")
            print()
    else:
        print("No books available in the library")
        print("---------------------------------------------")
        print()
        return library
    return library


