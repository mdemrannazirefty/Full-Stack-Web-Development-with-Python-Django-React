from Save_Books import Save_Books

def add_book(library):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    isbn = int(input("Enter Book Id: "))
    year= input("Enter Published Year: ")
    price = float(input("Enter Book Price: "))
    quantity = int(input("Enter Quantity: "))
    
    book = {"Title": title, "Author": author, "Isbn": isbn,"Year":year,"Price": price, "Quantity": quantity}
    if library is None:
        library = [] 
    
    library.append(book)
    Save_Books(library)
    print("Your Book Added Successfully")
    print()
    return library

   