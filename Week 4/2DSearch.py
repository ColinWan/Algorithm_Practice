import random
import os
import numpy as np
import matplotlib.pyplot as plt
directory = '/Users/colinwan/Desktop/Coursera_algo/Python/Week 4/kdtree'
class Node:
    def __init__(self, x, y, check=True):
        self.x = x
        self.y = y
        self.check = check
        self.left = None
        self.right = None
        # self.max = y

    def add(self, x, y):
        new_node = Node(x, y, not self.check)

        if self.check:
            if not self.left and x<self.x:
                self.left = new_node
            elif not self.right and x>self.x:
                self.right = new_node
            elif x<self.x:
                self.left.add(x, y)
            elif x>self.x:
                self.right.add(x, y)

        if not self.check:
            if not self.left and y<self.y:
                self.left = new_node
            elif not self.right and y>self.y:
                self.right = new_node
            elif y<self.y:
                self.left.add(x, y)
            elif y>self.y:
                self.right.add(x, y)

    def dist(self, x, y):
        return (self.x-x)**2 + (self.y-y)**2

    def closest_point(self, x, y, cur_champ=None):
        if not cur_champ: cur_champ = self
        if self.dist(x, y) < cur_champ.dist(x, y): cur_champ = self
        if self.check:
            if self.left and x < self.x:
                cur_champ = self.left.closest_point(x, y, cur_champ)
            elif self.right and x > self.x:
                cur_champ = self.right.closest_point(x, y, cur_champ)
            elif self.right and self.left:
                left_champ = self.left.closest_point(x, y, cur_champ)
                right_champ = self.right.closest_point(x, y, cur_champ)
                cur_champ = left_champ if left_champ.dist(x, y)<right_champ.dist(x, y) else right_champ
        elif not self.check:
            if self.left and y < self.y:
                cur_champ = self.left.closest_point(x, y, cur_champ)
            elif self.right and y > self.y:
                cur_champ = self.right.closest_point(x, y, cur_champ)
            elif self.right and self.left:
                left_champ = self.left.closest_point(x, y, cur_champ)
                right_champ = self.right.closest_point(x, y, cur_champ)
                cur_champ = left_champ if left_champ.dist(x, y)<right_champ.dist(x, y) else right_champ
        return cur_champ









    def show(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = str((self.x, self.y))
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = str((self.x, self.y))
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = str((self.x, self.y))
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = str((self.x, self.y))
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



data = np.loadtxt(directory+'/'+'input10K.txt', skiprows=1)

a = Node(data[0, 0], data[0, 1])
for i in range(data.shape[0]):
    a.add(data[i][0], data[i][1])
print('added')
p = np.random.random(2)
k = a.closest_point(p[0], p[1])

fig = plt.figure()
plt.scatter(data[:,0],data[:,1], s=0.3)
plt.scatter(p[0], p[1],s=0.3)
plt.scatter(k.x, k.y,s=0.3)
plt.xlim([0,1])
plt.ylim([0,1])
plt.show()

# for filename in os.listdir(directory):
#     if filename.endswith(".txt"):
#         print(filename)
#         data = np.loadtxt(directory+'/'+filename)
#