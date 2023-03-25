import re


def is_valid_email(email):
    """
    Check if string is a valid email.
    :param email: the email to validate
    :return: true or false
    """
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    return re.fullmatch(email_regex, email)
