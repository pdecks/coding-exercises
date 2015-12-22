class LL(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def append_node(self, data, next=None):
        new_node = Node(data, next)
        # check for head
        if not self.head:
            self.head = new_node

        # check for tail
        if self.tail:
            self.tail.next = new_node

        self.tail = new_node

    def remove_node(self, value):
        # check for head
        if self.head and self.head.data == value:
            self.head = self.head.next
            # because tail points to head ...
            self.tail.next = self.head
            return

        current = self.head
        while current.next.data != value:
            current = current.next
        # reassign tail before deleting node if node is tail
        if self.tail == current.next:
            self.tail = current.next.next
        # delete node by breaking link
        current.next = current.next.next

    def traverse_by_kill_every(self, kill_every):
        current = self.tail
        while self.head != self.tail:
            for i in range(kill_every):
                current = current.next
            self.remove_node(current.data)
        return self.head.data

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def find_survivor(num_ppl, kill_every):
    """Find the Josephus survivor given the number of people and skip number.
    Uses a LL where the tail points to the head.

    >>> find_survivor(10, 3)
    4

    >>> find_survivor(11, 2)
    7
    """

    # create the LL
    josephus_LL = LL()

    # append the nodes
    for i in range(1, num_ppl + 1):
        # point tail to head
        if i == num_ppl:
            josephus_LL.append_node(i, josephus_LL.head)    
        else:
            josephus_LL.append_node(i)

    # remove nodes by kill_every until head == tail (survivor)
    return josephus_LL.traverse_by_kill_every(kill_every)

if __name__ == "__main__":
    find_survivor(10, 3)
