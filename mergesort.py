def merge_sort(lst):
    """Implement top-down mergesort algorithm.

    >>> merge_sort([54, 2, 3, 9, 23, 8, 0, 4, 6])
    [0, 2, 3, 4, 6, 8, 9, 23, 54]
    """
    # check for one-item list
    if len(lst) < 2:
        return lst

    # recurse to split lists into one-item lists
    mid = len(lst) / 2
    lst1 = merge_sort(lst[:mid])
    lst2 = merge_sort(lst[mid:])

    # merge and sort lists
    merged_list = []
    while lst1 or lst2:
        if not lst1:
            merged_list.append(lst2.pop(0))
        elif not lst2:
            merged_list.append(lst1.pop(0))
        elif lst1[0] < lst2[0]:
            merged_list.append(lst1.pop(0))
        else:
            merged_list.append(lst2.pop(0))

    return merged_list
