def get_data():
    """Get data from database."""
    return ["user", "password", 26]


def save_data(data):
    """Save data to the database, and return True if successful."""
    return True


def do_manipulation():
    """Get data from the database, do manipulation, and save data back to the database."""
    data = get_data()
    if data:
        # do manipulation here
        return save_data(data)
    else:
        raise ValueError