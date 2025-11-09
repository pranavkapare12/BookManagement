<h1>Library Management System</h1>

A simple and interactive menu-driven Python application that manages a collection of books using Python dictionaries.
This project demonstrates core programming concepts such as data structures, functions, searching, sorting, and tabular data representation.

✅ Features

Add new books with ID, title, author, category, and price

Update existing book information

Delete books using Book ID

Search books by title, author, or price

Search by author (all books by a given author)

Search by category

Display all books in a formatted table using tabulate

Find highest-priced books (Top N sorting without built-in sort functions)

Input validation for numeric fields

Modular function-based code structure

✅ Tech Used

Python

tabulate library (for table formatting)

✅ How It Works

The project stores books inside a Python dictionary, where:
Key → Book ID
Value → Another dictionary containing book details


Example :
{
    1: {
        "Title": "Let Us C",
        "Author": "Yashavant Kanetkar",
        "Cate": "Coding",
        "Price": 3000.0
    }
}

Each Book entry contains :: 

| Field      | Description                |
| ---------- | -------------------------- |
| **Title**  | Name of the book           |
| **Author** | Author of the book         |
| **Cate**   | Category/genre of the book |
| **Price**  | Price of the book (float)  |

This makes it easy to:
Filter by category
Search by author or title
Sort by price
Update information
Display the entire collection cleanly

MENU Options
1. Add Book  
2. Update Book  
3. Delete Entry  
4. Display Books  
5. Search Book  
6. Exit  
7. Search by Author  
8. Search by Category  
9. Sort by Highest Price (Top N)
