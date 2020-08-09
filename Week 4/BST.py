import random
class Node:
    def __init__(self, val, parent=None):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None

    def add(self, val):
        if not self.left and val<self.val:
            self.left = Node(val, self)
        elif not self.right and val>self.val:
            self.right = Node(val, self)
        elif val<self.val:
            self.left.add(val)
        elif val>self.val:
            self.right.add(val)

    def max(self):
        c = self
        while c.right:
            c = c.right
        return c if c else self

    def min(self):
        c = self
        while c.left:
            c = c.left
        return c if c else self

    def delete(self, val):
        if self.val == val:
            print('This is the node')
            print(self.parent.val)
            print(self.parent.left.val)
            print(self.parent.right.val)
            if not self.right and not self.left:
                print('no left and right ', self.show())
                if self.parent.val <= self.val:
                    # print('The parent is ', self.parent.show())
                    print('removing parent right')
                    self.parent.right = None
                elif self.parent.val > self.val:
                    # print('The parent is ', self.parent.show())
                    print('removing parent left')
                    self.parent.left = None

            elif not self.right:
                print("No right")
                self.val, self.left, self.right = self.left.val, self.left.left, self.left.right
                if self.left: self.left.parent = self
                if self.right: self.right.parent = self
            elif not self.left:
                print('No left')
                self.val, self.left, self.right = self.right.val, self.right.left, self.right.right
                if self.left: self.left.parent = self
                if self.right: self.right.parent = self
            else:
                print('both left and right')
                temp = self.right.min()
                self.val = temp.val
                print('deleting from subtree')
                # self.right.show()
                self.right.delete(temp.val)
        elif self.val < val and self.right:
            print('deleting from right')
            self.right.delete(val)
        elif self.val > val and self.left:
            print('deleting from left')
            self.left.delete(val)

    def rotateleft(self):
        new_left = Node(self.val)
        new_left.left, new_left.right = self.left, self.right.left
        self.val = self.right.val
        self.right = self.right.right
        self.left = new_left


    def rotateright(self):
        new_right = Node(self.val)
        new_right.right, new_right.left = self.right, self.left.right
        self.val = self.left.val
        self.left = self.left.left
        self.right = new_right










    def show(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

a=Node(2)
a.add(3)
a.add(0)
a.show()
a.delete(0)
a.show()

# L = random.sample(range(0, 15), 14)
# # L=[5, 2, 1, 7, 9, 8]
#
#
# print(L)
# a = Node(L[0])
# for i in L[1:]:
#     a.add(i)
# a.show()
#
# c = None
# while len(L)>1:
#     c = random.sample(L,1)[0]
#     L.remove(c)
#     print('deleting ', c)
#     a.delete(c)
#     a.show()