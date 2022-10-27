customers = {
    'mel': {'username': 'mel', 'password': 'Deaner32', 'name': 'Mel Wilson'},
    'squash': {'username': 'squash', 'password': '545600', 'name': 'Sara Squash'},
    'bunsen': {'username': 'bunsen', 'password': 'DaisyDat8', 'name': 'Bunsen Honeydew'},
    'hoon': {'username': 'hoon', 'password': 'Keeper08@', 'name': 'Shannon Hoon'}
}

def get_by_username(username):
    return customers.get(username)