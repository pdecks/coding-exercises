def largest_sum(nums):
    """Given list of numbers, find shortest subsequence with largest sum.
    
    >>> largest_sum([1, 0, 3, -8, 4, -2, 3])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 4, -2, 3, -2])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 19, -20, 4, -2, 3, -2])
    [19]

    >>> largest_sum([1, 0, 3, -8, 0, -2, 20, 1, 1, -22, 0, -2, 22])
    [22]
    """
    # Our best (update as we find new bests)
    best_sum = 0
    start_of_best = 0
    end_of_best = -1  # (nothing)

    # Current sum and start
    current_sum = 0
    start_of_curr = 0

    for i, n in enumerate(nums):
        current_sum += n

        if current_sum > best_sum:
            # Best so far -- record this sum & its start and end
            best_sum = current_sum
            start_of_best = start_of_curr
            end_of_best = i
            
        if current_sum == best_sum and current_sum > 0:
            # Best so far -- record this sum & its start and end
            if (i - start_of_curr) < (end_of_best - start_of_best):
                best_sum = current_sum
                start_of_best = start_of_curr
                end_of_best = i

        if current_sum <= 0:
            # Dropped belonw 1, so we can't improve -- reset
            # start_of_best, to begin with next number
            start_of_curr = i + 1
            current_sum = 0

    return nums[start_of_best:end_of_best + 1]

largest_sum([1, 0, 3, -8, 0, -2, 20, 1, 1, -22, 0, -2, 22])

# largest_sum([1, 0, 3, -8, 4, -2, 3, -2])

# largest_sum([1, 0, 3, -8, 19, -20, 4, -2, 3, -2])