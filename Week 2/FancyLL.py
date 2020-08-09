class Node:
    def __init__(self, val, nex=None, prev=None):
        self.val = val
        self.nex = nex
        self.prev = prev
    def __str__(self):
        return str(self.val)

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.front = None
        self.back = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        c = self.front
        while index and c:
            c = c.nex
            index -= 1
        if not c:
            return -1
        return c

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """

        new_node = Node(val, nex=self.front)
        if self.front:
            self.front.prev = new_node
            self.front = new_node
        else:
            self.front = new_node
            self.back = new_node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val, prev=self.back)
        if self.back:
            self.back.nex = new_node
            self.back = new_node
        else:
            self.front = new_node
            self.back = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
        c = self.front
        while index-1 and c:
            c = c.nex
            index -= 1
        if c:
            if not c.nex:
                self.addAtTail(val)
            else:
                p = c.nex
                new_node = Node(val, nex=p, prev=c)
                p.prev = new_node
                c.nex = new_node


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        c = self.front
        while index and c:
            c = c.nex
            index -= 1
        if c:
            if not c.prev and not c.nex:
                self.back, self.front = None, None
            elif not c.prev:
                self.front = self.front.nex
                self.front.prev = None
            elif not c.nex:
                self.back = self.back.prev
                self.back.nex = None
            else:
                c.prev.nex = c.nex
                if c.nex: c.nex.prev = c.prev
                if not c.nex: self.back = c.prev


    def __str__(self):
        s = '|' + str(self.front)
        cur = self.front.nex
        while cur:
            s += '->' + str(cur)
            cur = cur.nex
        s += '|'
        return s

