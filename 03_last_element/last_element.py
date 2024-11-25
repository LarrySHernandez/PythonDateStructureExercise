def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if type(lst[len(lst) - 1]) is dict or type(lst[len(lst) - 1]) is list :
        return None
    else:
        return lst[len(lst) - 1]