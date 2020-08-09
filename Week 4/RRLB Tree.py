import random

class Node():
    def __init__(self, val, color=True, parent=None):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None
        self.color = color

    def rotateleft(self):
        new_left = Node(self.val, color=self.right.color, parent=self)
        new_left.left, new_left.right = self.left, self.right.left
        if self.right.left: self.right.left.parent = new_left
        if self.left: self.left.parent = new_left
        self.val = self.right.val
        self.right = self.right.right
        if self.right: self.right.parent = self
        self.left = new_left

    def rotateright(self):
        new_right = Node(self.val, color=self.left.color, parent=self)
        new_right.right, new_right.left = self.right, self.left.right
        if self.left.right: self.left.right.parent = new_right
        if self.right: self.right.parent=new_right
        self.val = self.left.val
        self.left = self.left.left
        if self.left: self.left.parent = self
        self.right = new_right

    def flip(self):
        self.color = not self.color
        self.left.color, self.right.color = not self.left.color, not self.right.color

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

    def add(self, val):
        if not self.left and val<self.val:
            self.left = Node(val, parent=self)
        elif not self.right and val>self.val:
            self.right = Node(val, parent=self)
        elif val<self.val:
            self.left.add(val)
        elif val>self.val:
            self.right.add(val)

        if self.right:
            if self.right.color and (not self.left or not self.left.color):
                # print('rotating left')
                # self.show()
                self.rotateleft()
        if self.left and self.left.left:
            if self.left.color and self.left.left.color:
                # print('rotating right')
                # self.show()
                self.rotateright()
        if self.right and self.left:
            if self.right.color and self.left.color:
                # print('flipping')
                self.flip()

    def delete(self, val):
        if self.val == val:
            # print('This is the node')
            if not self.right and not self.left:
                # print('no left and right ')
                if self.parent.val <= self.val:
                    # print('The parent is ', self.parent.show())
                    # print('removing parent right')
                    self.parent.right = None
                elif self.parent.val > self.val:
                    # print('The parent is ')
                    # self.parent.show()
                    # print('removing parent left')
                    self.parent.left = None

            elif not self.right:
                # print("No right")
                self.val, self.left, self.right, self.color = self.left.val, self.left.left, self.left.right, self.left.color
                if self.left: self.left.parent = self
                if self.right: self.right.parent = self
            elif not self.left:
                # print('No left')
                self.val, self.left, self.right, self.color = self.right.val, self.right.left, self.right.right, self.right.color
                if self.left: self.left.parent = self
                if self.right: self.right.parent = self
            else:
                # print('both left and right')
                temp = self.right.min()
                self.val = temp.val
                self.color = temp.color
                # print('deleting from subtree')
                # self.right.show()
                self.right.delete(temp.val)
        elif self.val < val and self.right:
            # print('deleting from right')
            self.right.delete(val)
        elif self.val > val and self.left:
            # print('deleting from left')
            self.left.delete(val)

        if self.right:
            if self.right.color and (not self.left or not self.left.color):
                print('rotating left')
                # self.show()
                self.rotateleft()
        if self.left and self.left.left:
            if self.left.color and self.left.left.color:
                print('rotating right')
                # self.show()
                self.rotateright()
        if self.right and self.left:
            if self.right.color and self.left.color:
                print('flipping')
                self.flip()











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
            indent = '<' if self.left.color else '/'
            second_line = (x) * ' ' + indent + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            indent = '>' if self.right.color else '\\'
            second_line = (u + x) * ' ' + indent + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        indent_left = '<' if self.left.color else '/'
        indent_right = '>' if self.right.color else '\\'
        second_line = x * ' ' + indent_left + (n - x - 1 + u + y) * ' ' + indent_right + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def numtoletter(L):
    r = ''
    for i in L:
        r +=chr(97+i)
    return r
L = random.sample(range(0, 26), 26)
L=[8, 24, 7, 16, 14, 21, 18, 1, 11, 6, 0, 19, 22, 3, 5, 17, 25, 12, 23, 9, 2, 15, 20, 10, 4, 13]
# L = numtoletter(L)


print(L)
a = Node(L[0], color=False)
for i in L[1:]:
    # print('current tree')
    print('adding ', i)
    a.add(i)
    a.show()



c = None
while len(L)>1:
    c = random.sample(L,1)[0]
    L.remove(c)
    print('deleting ', c)
    a.delete(c)
    a.show()
