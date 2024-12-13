import csv

def Save_Books(library):
    with open("libraryData.csv", mode="w", newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow(["Title", "Author", "Isbn","Year", "Price","Quantity"]) 
        # title,author,isbn,year,price,quantity
        for book in library:
            writer.writerow([book["Title"], book["Author"], book["Isbn"], book["Year"],book["Price"], book["Quantity"]])
            
