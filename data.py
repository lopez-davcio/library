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



"""
Only to be run to preload mock data

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
"""


    