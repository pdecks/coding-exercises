def check_sum_before_and_after_index(int_list):
    """Determine if there exists an element in the array such that the sum of
    the elements on its left is equal to the sum of the elements on its right.
    If there are no elements to the left/right, then the sum is considered to be
    zero.

    >>> int_lst = [1, 2, 3, 3]
    >>> check_sum_before_and_after_index(int_lst)
    YES

    """
    # a one-item list always meets this requirement
    if len(int_list) == 1:
        print "YES"
        return

    # for each integer, find the sum of all the integers
    # before it, storing the total product so far each time
    sum_of_all_ints_before_index = [None] * len(int_list)

    sum_so_far = 0
    for i in xrange(len(int_list)):
        sum_of_all_ints_before_index[i] = sum_so_far
        sum_so_far += int_list[i]

    # for each integer, find the sum of all the integers
    # after it, storing the total product so far each time
    sum_of_all_ints_after_index = [None] * len(int_list)

    sum_so_far = 0
    i = len(int_list) - 1
    while i >= 0:
        sum_of_all_ints_after_index[i] = sum_so_far
        sum_so_far += int_list[i]
        i -= 1

    # for each index, compare before / after entries
    for i in xrange(len(int_list)):
        if sum_of_all_ints_before_index[i] == sum_of_all_ints_after_index[i]:
            print "YES"
            return

    # if no number exists meeting the sum criteria
    print "NO"
    return

