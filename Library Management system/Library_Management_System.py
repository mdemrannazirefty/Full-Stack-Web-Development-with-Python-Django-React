## Library Management System
import Add_Book
import Remove_Book
import Save_Books
import Update_Book
import Search_Book
import View_All_Books

print("***** Welcome To Libary Management System *****")
laibary=[]

while True:
    print("@ Select any Option")
    print("1.Add Book")
    print("2.Remove Book")
    print("3.Search Book")
    print("4.Update Book")
    print("5.View All Books")
    print("6.Exit")

    option = int(input("- Enter your Option: "))
    if option==1:
        laibary=Add_Book.add_book(laibary)
    elif option==2:
        laibary=Remove_Book.remove_book(laibary)
    elif option==3:
        laibary=Search_Book.search_book(laibary)
    elif option==4:
        laibary=Update_Book.update_book(laibary)
    elif option==5:
        laibary=View_All_Books.view_all_books(laibary)
    elif option==6:
        print("Thanks for using Library Management System")
        print()
        break
    else:
        print("Invalid Option")
