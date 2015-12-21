def insertion_sort(lst):
    """Given a list, sort in place using insertion sort algorithm.

    >>> insertion_sort([6, 5, 3, 1, 8, 7, 2, 4])
    [1, 2, 3, 4, 5, 6, 7, 8]
    
    """
    for i in range(1, len(lst)):
        j = i
        x = lst[i]
        while j > 0 and lst[j-1] > x:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = x

    return lst