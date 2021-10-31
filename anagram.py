def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    x = ''.join(elem.lower() for elem in first_string if elem.isalpha())
    y = ''.join(elem.lower() for elem in second_string if elem.isalpha())

    if (sorted(x) == sorted(y)):
        return True
    else:
        return False


print(is_anagram("RACECAR", "rACEcar"))
