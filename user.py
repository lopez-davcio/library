import data

class User:
    """A class to model the library users and to store information related users"""

    def __init__(self, user_number, user_name):
        self.user_number = user_number
        self.user_name = user_name
       
        """Add user to users dictionary"""
        data.users[str(user_number)] = {'user_number':user_number, 'user_name':user_name, 'current_books':[], 'past_books':[]}

        

    