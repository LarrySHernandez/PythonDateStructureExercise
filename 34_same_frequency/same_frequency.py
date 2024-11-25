def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    my_list1 = str(num1)
    my_list2 = str(num2)
    my_set = set(str(num1))
    for num in my_set:
        count1 = my_list1.count(num)
        count2 = my_list2.count(num)
        if not count1 == count2:
            return False
    return True