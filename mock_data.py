from book import Book
from user import User 
import data

"""
Code to run only when mock info isn't in inventory_database.json and user_database.json 
"""

books_catalog = [
    ['handbook', 'ou', 40182],
    ['notebook', 'ax', 58703],
    ['manual', 're', 73219],
    ['guide', 'lm', 46874],
    ['journal', 'tz', 91562],
    ['ledger', 'vk', 64301],
    ['report', 'dn', 52987],
    ['catalog', 'sm', 38429],
    ['logbook', 'cy', 77740],
    ['register', 'xp', 82016],
    ['bulletin', 'fa', 31055],
    ['record', 'uj', 69834],
    ['paper', 'bo', 45972],
    ['folio', 'xz', 87319],
    ['briefing', 'ni', 59160],
    ['summary', 'qe', 74528],
    ['memo', 'kh', 62493],
    ['transcript', 'ld', 35210],
    ['outline', 'gw', 89974],
    ['synopsis', 'zb', 47086]
]

library_users = [
    [401, 'DLM'],
    [587, 'QRT'],
    [732, 'LNV'],
    [468, 'BXP'],
    [915, 'ZKC'],
    [643, 'MAJ'],
    [529, 'WUT'],
    [397, 'CKY'],
    [777, 'HGD'],
    [820, 'NRQ'],
    [310, 'JFL'],
    [698, 'TVS'],
    [459, 'UEM'],
    [873, 'XZD'],
    [591, 'RBA'],
    [261, 'KON'],
    [624, 'YMI'],
    [352, 'GEH'],
    [899, 'VDL'],
    [470, 'SQC']
]

def load_books():
    for book in books_catalog:
        name = book[0]
        author = book[1]
        isbn = book[2]
        Book(isbn, name, author)
load_books()        

def load_users():
    for user in library_users:
        number = user[0]
        name = user[1]
        User(number, name)
load_users()

data.save_inventory_users()

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