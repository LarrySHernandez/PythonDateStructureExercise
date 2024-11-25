def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    lst = list(phrase)
    for char in lst:
        if char.upper() == to_swap.upper():
            lst[lst.index(char)] = char.swapcase()

    return ''.join(lst)
