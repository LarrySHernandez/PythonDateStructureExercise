def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    lst = list(phrase)
    dct = {}
    vowels = ['a','e','i','o','u']
    count = 0
    for item in lst:
        if item.lower() in vowels:
            if dct[item]:
                dct[item] = count 
            else:
                dct[item] = count
    
    return dct