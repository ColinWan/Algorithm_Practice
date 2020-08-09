class LinkedListNode:
    def __init__(self, node=None, front=None, next=None):
        self.node = node
        self.front = front
        self.next = next

    def __str__(self):
        return str(self.node)

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, value):
        linkednode = LinkedListNode(value, front=self.last, next=None)
        if self.last:
            self.last.next = linkednode
            self.last = linkednode
        else:
            self.first = linkednode
            self.last = linkednode

    def add_first(self, value):
        linkednode = LinkedListNode(value, front=None, next=self.first)
        if self.first:
            self.first.front = linkednode
            self.first = linkednode
        else:
            self.first = linkednode
            self.last = linkednode

    def remove_first(self):
        # cur = self.first
        self.first = self.first.next
        return self.first.node

    def remove_last(self):
        # cur = self.last
        self.last = self.last.front
        return self.last.node

    def is_empty(self):
        return self.first is None

    def __str__(self):
        s = '|' + str(self.first)
        cur = self.first.next
        while cur:
            s+= '->' + str(cur)
            cur = cur.next
        s += '|'
        return s


