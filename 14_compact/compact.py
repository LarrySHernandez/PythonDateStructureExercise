def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    lst_copy =  []
    for item in lst:
        if bool(item):
           lst_copy.append(item)

    return lst_copy