"""Create a contacts application. You are given the number of operations to
perform, N. In any contacts application, two basic operations are add and find.
The input will be one of the following:

1. add name
2. find partial

Input Format

The first line contains the integer N, the number of operations to be performed. 
The next N lines contains one of the two operations defined above.

Constraints

1≤N≤105 
1≤Length(name)≤21 
1≤Length(partial)≤21

The entire input consists of lowercase characters only.

Output Format

For each operation of type find partial, print the number of contacts starting
with the string partial.
"""

class Trie_Node(object):

    def __init__(self, value=None):
        self.value = value
        self.count = 1
        self.children = {}

    def __insert__(self, word):
        "'apple' --> 'a' --> 'p' --> 'p' --> 'l' --> 'e' "
        curr_node = self
        i = 0
        while i < len(word) and curr_node.value != '*':
            c = word[i]
            # if no children exist yet, add first character
            if not curr_node.children:
                curr_node.children[c] = Trie_Node(c)
                curr_node = curr_node.children[c]
            # if there are children and 'c' is a child, move to next node
            elif curr_node.children.get(c, 0) != 0:
                curr_node = curr_node.children[c]
                curr_node.count += 1
            else:
                curr_node.children[c] = Trie_Node(c)
                curr_node = curr_node.children[c]
            i += 1
        # append '*' to signify leaf node at end of string
        curr_node.children['*'] = Trie_Node('*')


class Trie(object):

    def __init__(self):
        self.root = Trie_Node()

    def insert(self, word):
        self.root.__insert__(word)


trie = Trie()
trie.insert('apple')
trie.insert('ape')
trie.insert('apply')

