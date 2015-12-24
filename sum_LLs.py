class Linked_List(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def append_node(self, data, next=None):
        new_node = Node(data, next)

        if not self.head:
            self.head = new_node
        
        if self.tail:
            self.tail.next = new_node
        
        self.tail = new_node


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def sum_LLs(LL1, LL2):
    """Given 2 linked lists representing numbers by digit starting with 1s place,
    sum them and return the result.

    >>> LL1 = Linked_List()
    >>> LL1.append_node(7)
    >>> LL1.append_node(1)
    >>> LL1.append_node(6)
    >>> LL2 = Linked_List()
    >>> LL2.append_node(5)
    >>> LL2.append_node(9)
    >>> LL2.append_node(2)
    >>> sum_LLs(LL1, LL2)
    912

    """
    sum_num = 0
    curr_place = 0
    curr_digit = None
    carry_over = False

    # assuming passed 2 non-empty LLs
    curr_n1 = LL1.head
    curr_n2 = LL2.head

    while curr_n1 or curr_n2:
        if not curr_n1:
            dig1 = 0
            dig2 = curr_n2.data
            curr_n2 = curr_n2.next
        elif not curr_n2:
            dig2 = 0
            dig1 = curr_n1.data
            curr_n1 = curr_n1.next
        else:
            dig1 = curr_n1.data
            dig2 = curr_n2.data
            curr_n1 = curr_n1.next
            curr_n2 = curr_n2.next
        curr_digit, carry_over = add_digits(dig1, dig2, carry_over)
        sum_num += curr_digit * (10 ** curr_place)
        curr_place += 1
    if carry_over:
        sum_num += 1 * (10 ** curr_place)
    # curr_digit, carry_over = add_digits(curr_n1.data, curr_n2.data, carry_over)
    return sum_num


def add_digits(d1, d2, c_over):
    """Given two digits and boolean carry over, sum digits and return new carry
    over"""
    if c_over:
        result = d1 + d2 + 1
    else:
        result = d1 + d2
    if result > 9:
        result -= 10
        c_over = True
    else:
        c_over = False
    return result, c_over

if __name__ == "__main__":
    LL1 = Linked_List()
    LL1.append_node(7)
    LL1.append_node(1)
    LL1.append_node(6)
    LL1.append_node(7)

    LL2 = Linked_List()
    LL2.append_node(5)
    LL2.append_node(9)
    LL2.append_node(2)


summed_num = sum_LLs(LL1, LL2)
print "This is the sum:", summed_num

