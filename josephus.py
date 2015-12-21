def find_survivor(num_ppl, kill_every):
    """Find the Josephus survivor given the number of people and skip number.

    >>> find_survivor(10, 3)
    4

    >>> find_survivor(11, 2)
    7
    """
    # initialize list of True of length num_ppl
    ppl_list = [True] * num_ppl
    total_killed = 0
    last_killed = None  # result to return

    # count used for kill action
    count = 1
    # count for indexing
    i = 0

    while total_killed < num_ppl:
        if count % kill_every == 0:
            # kill person and update counter & return value
            ppl_list[i] = False
            total_killed += 1
            last_killed = i
        count += 1
        i += 1
        if i == num_ppl:
            i = 0
        # find people who are still alive
        while not ppl_list[i] and total_killed < num_ppl:
            i += 1
            # restart index if list length exceeded
            if i == num_ppl:
                i = 0

    return last_killed + 1

find_survivor(10, 3)