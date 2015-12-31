def condense_mtg_times(mtg_lst):
    """Given a list of (start, end) meeting time pairs, return a list of 
    condensed (start, end) meeting times.

    >>> mtg_lst = [(0, 1), (3, 5), (4, 8), (10, 12)]
    >>> condense_mtg_times(mtg_lst)
    [(0, 1), (3, 8), (10, 12)]

    """
    avail_times = [True] * 16 # 16 1/2-hr time slots in 8-hr workday
    # flip bit to 'False' if mtg in time slot
    for start, end in mtg_lst:
        for i in range(start, end + 1):
            if avail_times[i]:
                avail_times[i] = False

    # pass thru avail_times to create condensed tuples
    condense_times = []
    n_start = None
    n_end = None

    for k in range(len(avail_times)):
        if n_start is None and not avail_times[k]:
            n_start = k
            n_end = k
        elif not avail_times[k]:
            n_end = k
            if k == len(avail_times) - 1:
                condense_times.append((n_start, n_end))
        elif n_start is not None:
            condense_times.append((n_start, n_end))
            n_start = None
            n_end = None
        k += 1

    return condense_times

if __name__ == "__main__":
    mtg_lst = [(0, 1), (3, 5), (4, 8), (10, 12)]
    condense_mtg_times(mtg_lst)
    


