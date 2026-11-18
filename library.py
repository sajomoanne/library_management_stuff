import csv
import pandas as pd

file = "library_data.csv"

# load books from file
def load():
    with open(file, "r", newline="") as f:
        data = list(csv.DictReader(f))
        return data
    

# save books to file
def save(books):
    with open(file, "w", newline="") as f:
        fields = ["id", "title", "author", "status"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(books)

# find a book by id
def find(books, id):
    for b in books:
        if b["id"] == id:
            return b
    return None

# print table of books
def table(lst):
    df = pd.DataFrame(lst)
    print(df)

def add(books):
    id = input("\nenter book ID: ").strip()
    if id == "":
        print("book ID cannot be empty")
        return
    if find(books, id):
        print("book ID already exists")
        return

    title = input("enter book title: ").strip()
    author = input("enter author name: ").strip()

    if title == "" or author == "":
        print("title and author cannot be empty")
        return

    books.append({
        "id": id,
        "title": title,
        "author": author,
        "status": "Available"
    })

    save(books)
    print("book added successfully")

def display(books):
    print()
    if len(books) == 0:
        print("no books in the library")
    else:
        table(books)

def search(books):
    word = input("\n enter ID / title / author to search: ").strip().lower()

    if word == "":
        print("please enter smth")
        return

    found = []

    for b in books:
        if (word in b["id"].lower() or word in b["title"].lower() or word in b["author"].lower()):
            found.append(b)

    if len(found) == 0:
        print("no books found")
    else:
        print()
        table(found)

def issue(books):
    id = input("\nenter book ID to issue: ").strip()
    b = find(books, id)

    if b == None:
        print("book not found")
    elif b["status"] == "Issued":
        print("book is already issued")
    else:
        b["status"] = "Issued"
        save(books)
        print("book issued successfully")

def give_back(books):
    id = input("\nenter book ID to return: ").strip()
    b = find(books, id)

    if b == None:
        print("book not found")
    elif b["status"] == "Available":
        print("book was not issued")
    else:
        b["status"] = "Available"
        save(books)
        print("book returned successfully")

def delete(books):
    id = input("\nenter book ID to delete: ").strip()
    b = find(books, id)

    if b == None:
        print("book not found")
        return

    sure = input("are you sure? (y/n): ").strip().lower()

    if sure == "y":
        books.remove(b)
        save(books)
        print("book deleted successfully")
    else:
        print("cancelled")

def menu():
    print()
    print("=" * 45)
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")
    print("=" * 45)

books = load()


while True:
    menu()
    c = input("\nenter your choice: ").strip()

    if c == "1":
        add(books)
    elif c == "2":
        display(books)
    elif c == "3":
        search(books)
    elif c == "4":
        issue(books)
    elif c == "5":
        give_back(books)
    elif c == "6":
        delete(books)
    elif c == "7":
        print("thank you, bye")
        break
    else:
        print("invalid choice, enter 1 to 7")
