class UnknownColorException(Exception):
    def __init__(self, color):
        super().__init__(f'The color "{color}" is not a valid color!')


class UserInputNotAnIntegerException(Exception):
    def __init__(self, user_input):
        super().__init__(f'Input "{user_input}" is not an integer!')


class InputNumberNotInRangeException(Exception):
    def __init__(self, user_integer, range_min, range_max):
        super().__init__(f'Input number {user_integer} is not between {range_min} and {range_max}!')


class InputStringNotInRangeException(Exception):
    def __init__(self, user_string, min_size, max_size):
        super().__init__(f'Input string length {user_string} is not between {min_size} and {max_size}!')


class InputNotAnEmailException(Exception):
    def __init__(self, email):
        super().__init__(f'Input "{email}" is not a valid email address!')
