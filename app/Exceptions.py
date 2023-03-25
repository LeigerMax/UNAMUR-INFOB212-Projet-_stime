class UserInputNotAnIntegerException(Exception):
    def __init__(self, user_input):
        super().__init__(f'Input "{user_input}" is not an integer!')


class InputIntegerNotInRangeException(Exception):
    def __init__(self, user_integer, range_min, range_max):
        super().__init__(f'Input integer {user_integer} is not between {range_min} and {range_max}!')
