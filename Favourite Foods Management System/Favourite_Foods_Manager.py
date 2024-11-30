#Favourite Foods Manager
foods=[]
print("** Welcome To Favoutite Foods Management System **")

while True:
    print("1. Add Food")
    print("2. Remove Food")
    print("3. View Foods")
    print("4. Exit")
    print()
    option=int(input("Choose Any Option: "))

    if option==1:
        food=input("Enter your food name: ")
        if food in foods:
            print("Food already exists in the list")  
        else:
            foods.append(food)
            print("Your Food added in List" ,foods)
        print()
    elif option==2:
        removefood=input("Which food you want to remove: ")
        if removefood in foods:
            foods.remove(removefood)
            print("Food removed from list", foods )
            print()
        else:
            print("Food not found in list\n")
    elif option==3:
        if foods:
            print("Your Favourite Foods Are: ")
            for index,food in enumerate(foods, start=1):
                print(f"{index}. {food}")
        print()
    elif option==4:
        print("Thanks for using Favoutite Foods Management System.\nExit Successfull !!")
        break
    else:
        print("Invalid input !! \nPlease Choose Those Option.")
        print()


