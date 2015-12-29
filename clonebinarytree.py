"""Given the root of a binary tree, return the root node of the cloned tree."""

class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


def copy_tree(original):
    """Clone a binary tree using the root node."""
    # check for empty tree
    if not original:
        return

    # create new root node
    new_root = BinaryNode(original.data)

    # current node in cloned tree
    clone = new_root

    # step through original and clone simultaneously
    while original:
        if original.left and not clone.left:
            clone.left = BinaryNode(original.left.data)
            clone.left.parent = clone
            original = original.left
            clone = clone.left
        elif original.right and not clone.right:
            clone.right = BinaryNode(original.right.data)
            clone.right.parent = clone
            original = original.right
            clone = clone.right
        # move back up the tree
        else:
            original = original.parent
            clone = clone.parent

    return new_root

if __name__ == "__main__":
    test_tree = BinaryNode(2)
    test_tree.left = BinaryNode(3, test_tree)
    test_tree.left.left = BinaryNode(5, test_tree.left)
    test_tree.right = BinaryNode(6, test_tree)
    test_tree.right.left = BinaryNode(9, test_tree.right)

    cloned_test = copy_tree(test_tree)

            