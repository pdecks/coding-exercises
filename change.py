from itertools import combinations

money = {'p': 1, 'd': 10}

def coins(n):
    """Given number of coins, n, return set of possible change values.

    >>> coins(1) == {1, 10}
    True

    >>> coins(2) == {2, 11, 20}
    True

    >>> coins(3) == {3, 12, 21, 30}
    True

    >>> coins(4) == {4, 13, 22, 31, 40}
    True

    >>> coins(10) == {10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100}
    True
    """
    pairs = zip(range(n, -1, -1), range(n + 1))
    coin_set = set()
    for pair in pairs:
        coin_set.add(pair[0] * 1 + pair[1] * 10)
    return coin_set


if __name__ == "__main__":
    print coins(1)
    print coins(2)
    print coins(3)
    print coins(4)
    print coins(10)

    # python -m doctest -v change.py


    # FIRST ATTEMPT, no good
    # n_change = set()
    # for change in combinations(money.keys(), n):
    #     curr_change = 0
    #     for coin in change:
    #         curr_change += money[coin]
    #     n_change.add(curr_change)

    # return n_change
