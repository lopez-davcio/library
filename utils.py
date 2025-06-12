from book import Book
from user import User
import data
import random

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
    isbn = str(isbn)
    print("Please add the book's title:")
    title = input()
    print("Please add the book's author:")
    author = input()
    Book(isbn, title, author)
    print(f'Book {title} has been added')



def add_new_user():
    """Takes the user name as input, generates a random user number, checks that it's not in use, and instantiate a user object"""
    while True:
        user_number = random.randint(100,999)
        user_number = str(user_number)
        if user_number in data.users.keys():
            continue
        else:
            break
    print(f'The assigned user number of the new user is {user_number}.') 
    print('Please add the user name:')
    user_name = input()
    user_name = user_name.upper()
    User(user_number, user_name)      
    print(f'User {user_name} has been added')

           
def lend_book(book_isbn, user_number):
    """
    Check that book is owned by the library and that the user is registered in the library. Then lends the book to the user, assigns the user as current_user in that book entry and the book as current_book in the user entry.    
    """
    if book_isbn in data.inventory.keys():        
        if user_number in data.users.keys():
            if data.inventory[book_isbn]['current_user'] == 'library':
                data.inventory[book_isbn]['current_user'] = str(user_number)
                data.users[user_number]['current_books'].append(book_isbn)
            else:
                print(f'Book {book_isbn} is not available.')
        else:
            print(f'The user number {user_number} is not registered in the library.')
    else:
        print(f"The library does not own the book with isbn: {book_isbn}.")
       

    

def return_book(book_isbn, user_number):
    """
    Returns the book to the library, checks if the system recognises that user as the original borrower, assigns library as current borrower,
    adds the user as past borrowers of the book, adds the book as past books borrowed by the user and deletes the book from current books of user.
    """
    if book_isbn in data.inventory.keys(): 
        if data.inventory[book_isbn]['current_user'] == user_number:
            data.inventory[book_isbn]['current_user'] = 'library'
            data.inventory[book_isbn]['past_users'].append(user_number)
            data.users[user_number]['past_books'].append(book_isbn)

            try:
                data.users[user_number]['current_books'].remove(book_isbn)
            except:
                print('That isbn was not in the list of books borrowed by the user, please investigate further.')            

        else:
            print(f'The system does not recognize user {user_number} as the current borrower of book {book_isbn}.')
    else:
        print(f"The library does not own the book with isbn: {book_isbn}.")



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