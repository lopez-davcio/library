import data

class Book:
    """ A class to model the book object and to store lists related to book inventory and location"""

    def __init__(self, isbn, name, author):
        self.isbn = isbn
        self.name = name
        self.author = author

            
        """Add book to inventory dictionary"""
        data.inventory[isbn] = {'isbn':self.isbn, 'name':self.name, 'author':self.author, 'current_user': 'library', 'past_users': []}

        