from database import User
from pypasswords import hash_it


def check_inputs_login(username, password):

    if username:
        if len(username) < 7:
            return 'Username should be more than 6 characters'
        elif len(username) > 31:
            return 'Username should be less than 32 characters'
    else:
        return 'Enter username'

    if password:
        if len(password) < 7:
            return 'Password should be more than 6 characters'
    else:
        return 'Enter password'

    return None  # if everything's fine


def check_inputs_signup(username, password, confirm_password):

    found_user = User.query.filter_by(username=hash_it(username)).first()
    if found_user:
        return 'Username already exists'

    if username:
        if len(username) < 7:
            return 'Username should be more than 6 characters'
        elif len(username) > 31:
            return 'Username should be less than 32 characters'
    else:
        return 'Enter username'

    if password:
        if len(password) < 7:
            return 'Password should be more than 6 characters'
    else:
        return 'Enter password'

    if not confirm_password:
        return 'Confirm entered password'

    if password != confirm_password:
        return 'Passwords do not match'

    return None  # if everything's fine
