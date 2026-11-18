# Library Management System

A simple command-line library management system built with Python. Track books, manage availability status, and perform CRUD operations on your library collection.

## Features

- Add new books to the library
- Display all books in a table format
- Search books by ID, title, or author
- Issue books (mark as "Issued")
- Return books (mark as "Available")
- Delete books from the library

## Requirements

- Python 3.x
- pandas

## Setup

1. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install pandas
```

## Usage

Run the application:
```bash
python library.py
```

Follow the on-screen menu to perform operations:
1. Add Book
2. Display All Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Exit

## Data

Book data is stored in `library_data.csv` with fields:
- id: Unique book identifier
- title: Book title
- author: Author name
- status: "Available" or "Issued"
