def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lst = phrase.split(' ')
    for word in lst:
        lst[lst.index(word)] = word.capitalize()
        
    return ' '.join(lst)