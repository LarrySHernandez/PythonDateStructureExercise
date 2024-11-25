def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    total = 0
    count = 0
    max = len(matrix[0])
    while(count < max):
        total += matrix[count][count]
        count += 1
    print(count)
    count = 0
    max2 = max - 1
    while(count < max):
        total += matrix[max2][count]
        count += 1
        max2 -= 1
    return total