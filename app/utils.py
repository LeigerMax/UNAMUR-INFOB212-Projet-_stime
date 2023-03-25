import re
import sys

from app.view.console_utils.io import print_leave


def is_valid_email(email):
    """
    Check if string is a valid email.
    :param email: the email to validate
    :return: true or false
    """
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    return re.fullmatch(email_regex, email)


def exit_stime():
    """ Exit safely the program. """

    # TODO: close db connection
    print_leave()
    sys.exit(0)
