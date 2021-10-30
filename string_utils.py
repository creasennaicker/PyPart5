def str_len(str_in: str) -> int:
    """
    Given a string parameter, this function should return the length of the parameter.
    :type str_in: object
    :rtype: object
    """
    string_length = len(str_in)
    return string_length


print(str_len('PYTHON'))


def first_char(str_in: str) -> str:
    """
    Given a string parameter, this function should return the first letter of the parameter.
    """
    first_char_yo = str_in[0]
    return first_char_yo


print(first_char('python'))


def last_char(str_in: str) -> str:
    """
    Given a string parameter, this function should return the last letter of the parameter..
    """
    length = len(str_in)

    last_string_char = str_in[length - 1]

    return last_string_char


print(last_char('python'))


def input_has_substring(str_in: str, sub_str_in: str) -> bool:
    """
    This function determines if the substring exists within the string. Returns True or False.
    :type sub_str_in: object
    """

    if sub_str_in in str_in:
        return True
    else:
        return False


print(input_has_substring('python', 'p'))


def substring(str_in: str, start: int, stop: int) -> str:
    """
    Returns the substring of a string.

    Keyword arguments:
    str_in -- the string in which to generate a substring from
    start -- starting position of the input parameter to start the substring (inclusive)
    stop -- stopping position of the input parameter to stop the substring (exclusive)
    :rtype: object
    """
    input = str_in
    print(input[start:stop])



substring("python is super cool", 0, 5)


def opposite_case(str_in: str) -> str:
    """
    Given a string parameter, this function returns the same string back with each letter having the opposite case.
    Example: 
    When input = "Python" the function returns "pYTHON"
    :rtype: object
    """

    return str_in.swapcase()


print(opposite_case("Python"))
