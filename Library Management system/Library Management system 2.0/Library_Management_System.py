## Library Management System CLI
from Add_Book import add_book
from Remove_Book import remove_book
from Save_Books import Save_Books
from Update_Book import update_book
from Search_Book import search_book
import Load_Books
from View_All_Books import view_all_books
from datetime import datetime
from Lend_Book import lend_book
from Return_Book import return_book
from View_All_Lend import view_all_lend


print("***** Welcome To Libary Management System *****")

library=Load_Books.load_books([])
#lend_data_file = "lendData.json"

while True:
    print("@ Select any Option")
    print("1.Add Book")
    print("2.Remove Book")
    print("3.Search Book")
    print("4.Update Book")
    print("5.View All Books")
    print("6.Lend Book")
    print("7.Return Book")
    print("8.View All Lend")
    print("9.Exit")

    try:
        option = int(input("- Enter your Option: "))
    except ValueError:
        print("Invalid Input. Enter a number between (1-9)")
        print()
        continue
    
    if option==1:
        library=add_book(library)
    elif option==2:
        library=remove_book(library)
    elif option==3:
        library=search_book(library)
    elif option==4:
        library= update_book(library)
    elif option==5:
        view_all_books(library)
    elif option==6:
        library = lend_book(library)
    elif option==7:
        library = return_book(library)
    elif option == 8:
        view_all_lend()
    elif option==9:
        Save_Books(library) 
        print("Thanks for using Library Management System")
        print()
        break
    

    else:
        print("Invalid Option")
