from book import Book
from user import User
import utils
import data

"""
Simulate a database loading books and users from module data
"""

menu_print = """
Select an option:
1.  Add new book
2.  Add new user
3.  Lend book
4.  Return book
5.  Display all library users
6.  Display full inventory
7.  Display available books
8.  Display book location
9.  Display book info
10. Display book past borrowers
11. Display user's current book
Q. Quit
"""

"""
Load inventory_database and user_database at program initiation
"""
data.load_inventory_users()


while True:
    print(menu_print)
    choice = input()
    if choice == '1':
        print('You chose: Add new book.')
        utils.add_new_book()
    elif choice == '2':
        print('You chose: Add new user.')
        utils.add_new_user()    
    elif choice == '3':
        print('You chose: Lend book.')
        utils.lend_book()
    elif choice == '4':
        print('You chose: Return book.')
        utils.return_book()
    elif choice.lower() == 'q':
        data.save_inventory_users()
        break

    
    


"""
Save inventory in inventory_database and users in user_database

data.save_inventory_users()
"""