import data

class Book:
    """ A class to model the book object and to store lists related to book inventory and location"""

    def __init__(self, isbn, name, author):
        self.isbn = isbn
        self.name = name
        self.author = author

        self.current_user = 'library'
        self.past_users = dict()
        
        """A list of all the books that the library owns in which keys are isbn and value the book object"""
        data.inventory[isbn] = self

