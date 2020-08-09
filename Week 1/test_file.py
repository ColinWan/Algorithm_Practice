import numpy as np
import os
directory = '/Users/colinwan/Desktop/Coursera_algo/Python/percolation'

def root(base, x):
    while not (np.equal(base[:, max(0, x[0]), max(0, x[1])].flatten()[:2], x).all() or x[0]==-1):
        # print(x)
        x = base[:2, x[0], x[1]].astype(int)
    return x

def union(base, x, y):
    # print('x',x[0], x[1])
    # print('y',y[0], y[1])

    a = root(base, x)
    b = root(base, y)
    # print('a',a[0], a[1])
    # print('b',b[0], b[1])
    if (a!=b).any():
        base[:2, b[0], b[1]] = a

def percolation(l, size):
    l = (l-1).astype(int)
    size = int(size)
    if size==1 and list(l):
        return np.full([3, 1, 1], -1)
    xv, yv = np.meshgrid(np.arange(size), np.arange(size))
    b = np.full([size, size], False)
    base = np.empty((3, size, size))
    base[0, :, :] = yv
    base[1, :, :] = xv
    base[2, :, :] = b
    # base[:2, 0, :] = 0
    # print(base)
    for i in l:
        base[2, i[0], i[1]] = True
    for i in l[:10]:
        print('updating', i)
        if i[0] > 0 and base[2, i[0]-1, i[1]]:
            print('update upper')
            union(base, i, [i[0]-1, i[1]])
        if i[1] > 0 and base[2, i[0], i[1]-1]:
            print('update left')
            union(base, i, [i[0], i[1]-1])
        if i[0] < size-1 and base[2, i[0]+1, i[1]]:
            print('update lower')
            union(base, i, [i[0]+1, i[1]])
        if i[1] < size-1 and base[2, i[0], i[1]+1]:
            print('update right')
            union(base, i, [i[0], i[1]+1])
        print(base[:2, :, :])
    return base.astype(int)

filename = 'input2_no.txt'
data = np.loadtxt(directory+'/'+filename, skiprows=1)
size = np.loadtxt(directory+'/'+filename, usecols=(0))[0]
print(filename)

result = percolation(data, size)

if result is None:
    print(False)
else:
    root_list = [list(root(result, i)) for i in result[:2, -1, :].T]
    top_root_list = [list(root(result, i)) for i in result[:2, 0, :].T]
    i = 0
    while i < len(root_list):
        if root_list[i] in top_root_list:
            print(True)
            i = len(root_list)
        i += 1




















# member = [0, 1, 2, 3, 4, 5, 6]
# timestamp = [[(1, 2), (3, 4), (5, 6)], [(0, 1), (2, 3)], [(4, 5)]]
#
# def r(l, x):
#     while l[x]!=x:
#         x = l[x]
#     return x
#
# def u(l, p):
#     l[p[1]] = r(l, p[0])
#     return l
#
# def test(member, timestamp):
#     f = member
#     b = False
#     i = 0
#     while not b:
#         print('i: ', i)
#         for j in timestamp[i]:
#             f = u(f, j)
#
#         t = [r(f, k) for k in f]
#         print("f: ", f)
#         b = t[1:] == t[:-1]
#         print(b)
#         i += 1
#     return f
# f = test(member, timestamp)