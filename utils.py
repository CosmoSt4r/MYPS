def check_inputs(username, password):

    if username:
        if len(username) < 7:
            return 'Username should be more than 6 characters'
    else:
        return 'Enter username'

    if password:
        if len(password) < 7:
            return 'Password should be more than 6 characters'
    else:
        return 'Enter password'

    return None  # if everything's fine
