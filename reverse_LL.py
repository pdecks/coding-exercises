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

ll = Node(1, Node(2, Node(3)))
ll.as_string()
ll.reverse_LL(ll).as_string()