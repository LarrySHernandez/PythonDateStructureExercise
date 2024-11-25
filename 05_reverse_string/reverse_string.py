def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    lst = list(phrase)
    lst.reverse()
    reversed = ""
    for char in lst:
        reversed += char
    return reversed