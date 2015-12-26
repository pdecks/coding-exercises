"""Cracking the Coding Interview Problem 4.3

Given a binary tree, design an algorithm that creates a linked list of all the
nodes at each depth (e.g. if you have a tree with depth D, you'll have D linked
lists)

Make a binary search tree ...

>>> tree3 = make_bst([1, 2, 3])
>>> tree3.data
2

Make the list of Linked Lists ...

>>> list_of_LL3 = tree_depth_LL(tree3)
>>> list_of_LL3[1].tail.data == tree3.right
True

Make another binary search tree and its list of LL ...

>>> tree6 = make_bst([1, 2, 3, 4, 5, 6])
>>> list_of_LL6 = tree_depth_LL(tree6)

>>> list_of_LL6[2].tail.data == tree6.right.left
True

"""
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


class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, val):
        if val > self.data:
            if not self.right:
                self.right = BinaryNode(val)
            else:
                self.right.insert(val)
        else:
            if not self.left:
                self.left = BinaryNode(val)
            else:
                self.left.insert(val)


def make_bst(nums):
    """Given a list of sorted numbers, make a binary search tree.

    Returns the root node of a new BST that is valid and balanced.
    """
    if not nums:
        return None
    
    median = len(nums) / 2
    node = BinaryNode(nums[median])
    node.left = make_bst(nums[:median])
    node.right = make_bst(nums[median + 1:])

    return node


def tree_depth_LL(tree):
    if not tree:
        return None
    levels = {}
    visited = set()
    k = 1
    curr_node = tree
    pre_order_traversal(curr_node, levels, k, visited)

    linked_lists = []
    for k, lst in levels.items():
        curr_LL = Linked_List()
        for item in lst:
            curr_LL.append_node(item)
        linked_lists.append(curr_LL)

    return linked_lists


def pre_order_traversal(node, depth_dict, k, visited):
    if node:
        depth_dict.setdefault(k, []).append(node)
        visited.add(node)
        k += 1
        pre_order_traversal(node.left, depth_dict, k, visited)
        pre_order_traversal(node.right, depth_dict, k, visited)
    return




if __name__ == "__main__":

    tree3 = make_bst([1, 2, 3])
    tree3.data

    list_of_LL3 = tree_depth_LL(tree3)

    tree6 = make_bst([1, 2, 3, 4, 5, 6])
    list_of_LL6 = tree_depth_LL(tree6)