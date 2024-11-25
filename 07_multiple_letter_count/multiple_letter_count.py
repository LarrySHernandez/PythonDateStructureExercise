def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    ltr_count = {}
    for char1 in phrase:
        count = 0
        for char2 in phrase:
            if char1 == char2:
                count += 1
        ltr_count[char1] = count
    return ltr_count