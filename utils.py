from book import Book
from user import User
import data

"""A module for the logic of the library's operations"""



def add_new_book():
    """Ask input from user, book title author and isbn, checks that the isbn is a 5 digit number and add new book to inventory"""
    print('Please add a 5 digit isbn:')
    while True:
        isbn = input()
        if len(isbn) == 5:
            try:
                isbn = int(isbn)
                break
            except ValueError:
                print('The isbn must be a 5 digit number, please try again:')
        else:
            print('The isbn must be a 5 digit number, please try again:')
            continue
    print("Please add the book's title:")
    title = input()
    print("Please add the book's author:")
    author = input()
    Book(isbn, title, author)



def add_new_user():
    """Takes the user name as input, generates a random user number, checks that it's not in use, and instantiate a user object"""
    
    
            
    
def lend_book(book_isbn, user_number):
    """
    Lends a book to a user, checks that it's in stock and assigns the user to be the borrower in both book and user objects    
    """
    pass
       

    

def return_book():
    """
    Returns the book to the library, checks if the system recognises that user as the original borrower, assigns library as current borrower,
    adds the user as past borrowers of the book, adds the book as past books borrowed by the user and deletes the book from current books of user.
    """
    pass
   



def display_users():
    pass
        


def display_inventory():
    pass



def display_available_books():
    pass


def display_book_location():
    pass



def display_book_info():
    pass
    

def display_book_past_borrowers():
    pass



def display_user_current_book():
    pass