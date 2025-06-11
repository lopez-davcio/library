from pathlib import Path
import json

"""
A  module serving as a database to save all the information from execution to execution
"""


"""
A dictionary of all the books that the library owns in which keys are isbn and values are book attributes
"""
inventory = dict()


"""
A dict of dicts to store the utils's users, key = user_number, value = user object
"""
users = dict()


def load_data(file_address):
    try:
        path = Path(file_address)
        contents = path.read_text()
    except FileNotFoundError:
        print('A file seems to be missing')
    else:
        content_json = json.loads(contents)
        return content_json
    

def save_data(file_address,data):
    try:
        path = Path(file_address)
        content_json = json.dumps(data)
        path.write_text(content_json)
    except FileNotFoundError:
        print('It seems there is a missing file')


def load_inventory_users():
    global inventory, users
    inventory = load_data('inventory_database.json')
    users = load_data('user_database.json')

def save_inventory_users():
    save_data('inventory_database.json', inventory)
    save_data('user_database.json', users)






    