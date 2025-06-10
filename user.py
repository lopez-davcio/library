import data

class User:
    """A class to model the library users and to store information related users"""

    def __init__(self, user_number, user_name):
        self.user_number = user_number
        self.user_name = user_name
       
        """Books that the user currently holds"""
        self.current_book = dict()
        """Books that the user borrowed in the past"""
        self.past_books = dict()

        

    def __str__(self):
        pass