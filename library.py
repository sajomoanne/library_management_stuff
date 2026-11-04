import json
import os

file = "library_data.json"

# load books from file
def load():
    if os.path.exists(file):
        try:
            f = open(file)
            data = json.load(f)
            f.close()
            return data
        except:
            return []
    return []

# save books to file
def save(books):
    f = open(file, "w")
    json.dump(books, f)
    f.close()

# find a book by id
def find(books, id):
    for b in books:
        if b["id"] == id:
            return b
    return None

# print table of books
def table(lst):
    print("=" * 85)
    print(f"{'ID':<10}{'Title':<32}{'Author':<25}Status")
    print("=" * 85)
    for b in lst:
        print(f"{b['id'][:10]:<10}{b['title'][:29]:<32}{b['author'][:22]:<25}{b['status']}")
    print("=" * 85)

def add(books):
    id = input("\nEnter Book ID: ").strip()
    if id == "":
        print("Book ID cannot be empty!")
        return
    if find(books, id):
        print("Book ID already exists!")
        return
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()
    if title == "" or author == "":
        print("Title and author cannot be empty!")
        return
    books.append({"id": id, "title": title, "author": author, "status": "Available"})
    save(books)
    print("Book added successfully!")

def display(books):
    print()
    if len(books) == 0:
        print("No books in the library.")
    else:
        table(books)

def search(books):
    word = input("\nEnter ID, title or author to search: ").strip().lower()
    if word == "":
        print("Search cannot be empty!")
        return
    found = []
    for b in books:
        if word in b["id"].lower() or word in b["title"].lower() or word in b["author"].lower():
            found.append(b)
    if len(found) == 0:
        print("No books found.")
    else:
        print()
        table(found)

def issue(books):
    id = input("\nEnter Book ID to issue: ").strip()
    b = find(books, id)
    if b == None:
        print("Book not found!")
    elif b["status"] == "Issued":
        print("Book is already issued!")
    else:
        b["status"] = "Issued"
        save(books)
        print("Book issued successfully!")

def give_back(books):
    id = input("\nEnter Book ID to return: ").strip()
    b = find(books, id)
    if b == None:
        print("Book not found!")
    elif b["status"] == "Available":
        print("Book was not issued!")
    else:
        b["status"] = "Available"
        save(books)
        print("Book returned successfully!")

def delete(books):
    id = input("\nEnter Book ID to delete: ").strip()
    b = find(books, id)
    if b == None:
        print("Book not found!")
        return
    sure = input("Are you sure? (y/n): ").strip().lower()
    if sure == "y":
        books.remove(b)
        save(books)
        print("Book deleted successfully!")
    else:
        print("Cancelled.")

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

try:
    while True:
        menu()
        c = input("\nEnter your choice: ").strip()
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
            print("Thank you, bye!")
            break
        else:
            print("Invalid choice, enter 1 to 7.")
except (KeyboardInterrupt, EOFError):
    print("\nBye!")