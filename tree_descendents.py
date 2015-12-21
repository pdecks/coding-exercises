class Node(object):
    def __init__(self, name, children=None):
        self.name = name
        self.children = children
    
    # non-recursive solution
    # def count_descendents(self):
    #     if not self.children:
    #         return 0
    #     count = 0
    #     to_visit = self.children
    #     while to_visit:
    #         curr_node = to_visit.pop()
    #         count += 1
    #         if curr_node.children:
    #             to_visit.extend(curr_node.children)
    #     return count

    # recursive solution
    def count_descendents(self):
        if not self.children:
            return 0
        count = 0
        for child in self.children:
            count += 1 + child.count_descendents()
        return count

henri = Node("Henri")
nora = Node("Nora", [henri])
nick = Node("Nick")
janet = Node("Janet", [nick, nora])
al = Node("Al")
bob = Node("Bob")
jen = Node("Jen")
jessica = Node("Jessica", [al, bob, jen])
jane = Node("Jane", [jessica, janet])

jane.count_descendents()


