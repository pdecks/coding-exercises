"""Sunny and Johnny together have M dollars they want to spend on ice cream.
The parlor offers N flavors, and they want to choose two flavors so that they
end up spending the whole amount."""

def ice_cream_flavors(int_list, money_amt):
    """Given the cost of these flavors, display the indices of the two flavors
    whose sum is M. 

    >>> ice_cream_flavors([1, 4, 5, 3, 2], 4)
    1 4

    """
    # if flavor cost is greater than money amount, skip flavor
    # sub_list = [x in int_list if x < money_amt]
    for i in range(len(int_list)):
        # import pdb; pdb.set_trace()
        if int_list[i] < money_amt:
            difference = money_amt - int_list[i]
            for j in range(i + 1, len(int_list)):
                if int_list[j] == difference:
                    print "%d %d" % (i + 1, j + 1)
                    return
        else:
            continue

        return


def faster_ice_cream_flavors(int_list, money_amt):
    """Achieve O(n) running time by storing the ice cream flavor prices in a
    hashtable. So then you would just iterate through each of the prices, subtract
    the price from the money M that you have to spend, and then look up the
    difference in your hash table to see if there exists a flavor for that
    price. This would yield a runtime of O(n) + O(n) * O(1) = O(n).

    >>> faster_ice_cream_flavors([1, 4, 5, 3, 2], 4)
    1 4
    """
    flavor_dict = {}
    for i, cost in enumerate(int_list):
        flavor_dict[cost] = i + 1

    for i, cost in enumerate(int_list):
        if flavor_dict.get(money_amt - cost, 0) != 0:
            print "%d %d" % (i + 1, flavor_dict[money_amt - cost])
            return 
    return

if __name__ == "__main__":
    ice_cream_flavors([1, 4, 5, 3, 2], 4)
    faster_ice_cream_flavors([1, 4, 5, 3, 2], 4)