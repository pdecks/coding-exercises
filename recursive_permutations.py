def get_permutations(string):
    # base case
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    # recursive call: get all possible permutations for all chars except last
    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)

    # put the last char in all possible positions for each of the above permutations
    possible_positions_to_put_last_char = range(len(all_chars_except_last)+1)
    permutations = set()
    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in possible_positions_to_put_last_char:
            permutation = permutation_of_all_chars_except_last[:position] + last_char + permutation_of_all_chars_except_last[position:]
            permutations.add(permutation)

    return permutations

get_permutations('cats')