import csv
def load_books():
    try:
        with open("libraryData.csv", mode="r") as file:
            reader = csv.DictReader(file)
            return [
                {
                    "Title": row["Title"],
                    "Author": row["Author"],
                    "Isbn": int(row["Isbn"]),
                    "Year": row["Year"],
                    "Price": float(row["Price"]),
                    "Quantity": int(row["Quantity"])
                }
                for row in reader
            ]
    except FileNotFoundError:
        return []
    
    