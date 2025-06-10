from book import Book
import utils
import data

"""
Simulate a database loading books and users from module data
"""

"""
Code to run first time to save mock books, users, and transactions:
"""
def load_books():
    for book in data.books_catalog:
        name = book[0]
        author = book[1]
        isbn = book[2]
        Book(isbn, name, author)
load_books()        
print(data.inventory.keys())   
def load_users():
    pass

"""    
def load_mock_transactions():
    utils.lend_book(52987, 261)
    utils.lend_book(40182, 401)
    utils.lend_book(40182, 397)
    utils.lend_book(87319, 401)
    utils.return_book(87319, 401)
    utils.return_book(40182, 401)
    utils.lend_book(87319, 397)
    utils.lend_book(40182, 261)
    utils.return_book(52987, 261)
    utils.lend_book(52987, 401)
    utils.return_book(40182, 261)
"""

print("""
Select an option:
1. Add new book
2. Add new user
3. Lend book
4. Return book
5. Display all library users
6. Display full inventory
7. Display available books
8. Display book location
9. Display book info
10. Display book past borrowers
11. Display user's current book
Q. Quit
""")