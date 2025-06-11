from book import Book
from user import User
import utils
import data

"""
Simulate a database loading books and users from module data
"""

"""
Code to run only first time to save mock books, users, and transactions:

def load_books():
    for book in data.books_catalog:
        name = book[0]
        author = book[1]
        isbn = book[2]
        Book(isbn, name, author)
load_books()        
print(data.inventory.keys())   

def load_users():
    for user in data.library_users:
        number = user[0]
        name = user[1]
        User(number, name)
load_users()
print(data.users.keys())
"""

"""
Load inventory_database and user_database at program initiation
"""
data.load_inventory_users()


"""
Save inventory in inventory_database and users in user_database

data.save_inventory_users()
"""
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

