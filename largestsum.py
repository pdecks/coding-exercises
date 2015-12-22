def largest_sum(nums):
    """Given list of numbers, find shortest subsequence with largest sum.
    
    >>> largest_sum([1, 0, 3, -8, 4, -2, 3])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 4, -2, 3, -2])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 19, -20, 4, -2, 3, -2])
    [19]
    """
    # variables for keeping track of max sum
    max_seq = []
    max_index = len(nums) - 1
    max_sum = 0
    max_length = len(nums)
    
    # variables for current sum
    curr_sum = 0
    curr_length = 0
    i = 0  # start index
    j = 0  # end index

    while i <= max_index and j <= max_index:
        # skip negative numbers
        if nums[i] < 0:
            i += 1
            j = i
        # last value in index
        elif i == max_index:
            if nums[i] > max_sum:
                max_sum = nums[i]
                max_seq = nums[i:]
        else: # examine number and sequential values
            curr_sum = nums[i]
            curr_length = 1
            if curr_sum > max_sum or (curr_sum == max_sum and curr_length < max_length):
                max_sum = curr_sum
                max_length = curr_length
                if j + 1 < max_index:
                    max_seq = nums[i:j+1]
                else:
                    max_seq = nums[i:]
            while j <= max_index:
                # if next entry yields sum greater than 0
                if ((j + 1) < max_index and curr_sum + nums[j + 1] > 0) or ((j + 1) == max_index and nums[j + 1] > 0):
                    j += 1
                    curr_sum += nums[j]
                    curr_length += 1
                    if curr_sum > max_sum or (curr_sum == max_sum and curr_length < max_length):
                        max_sum = curr_sum
                        max_length = curr_length
                        if j + 1 <= max_index:
                            max_seq = nums[i:j+1]
                        else:
                            max_seq = nums[i:]

                # else move i to next positive number and start over
                elif (j + 2) <= max_index:
                    i = j+2
                    j = i
                    curr_sum = 0
                    curr_length = 0
                    break # go to outer while
                else:
                    j += 1

    return max_seq

# largest_sum([1, 0, 3, -8, 4, -2, 3, -2])

# largest_sum([1, 0, 3, -8, 19, -20, 4, -2, 3, -2])