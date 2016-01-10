class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
     
    def as_string(self):
        out = []
        n = self
        while n:
            out.append(str(n.data))
            n = n.next
        return "".join(out)

    def reverse_LL(self, head):
        prev = None
        curr = head
        while curr.next:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        if prev:
            curr.next = prev
        return curr

class Node2(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
       
    def as_string(self):
        out = []
        n = self
        while n:
            out.append(str(n.data))
            n = n.next
        return "".join(out)

    def reverse_LL(self, head):
        curr = head
        prev = None
        next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
      
        return prev


ll = Node(1, Node(2, Node(3)))
print ll.as_string()
print ll.reverse_LL(ll).as_string()

ll2 = Node2(1, Node2(2, Node2(3)))
print ll2.as_string()
print ll2.reverse_LL(ll).as_string()