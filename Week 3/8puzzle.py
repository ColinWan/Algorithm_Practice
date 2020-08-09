import numpy as np
import math

def swim(L, ind):
    c = L[ind][0]
    while ind >= 2 and L[ind // 2][0] >= c:
        L[ind], L[ind // 2] = L[ind // 2], L[ind]
        ind = ind // 2

def sink(L, ind, end=None):
    c = L[ind][0]
    ind = ind * 2 + 1 if ind * 2 + 1 < len(L[:end]) and L[ind * 2] < L[ind * 2 + 1] else ind * 2
    while ind < len(L[:end]) and L[ind][0] <= c:
        L[ind], L[ind // 2] = L[ind // 2], L[ind]
        ind = ind * 2 + 1 if ind * 2 + 1 < len(L[:end]) and L[ind * 2][0] < L[ind * 2 + 1][0] else ind * 2

def H_dis(L, T):
    c = 0
    for i in range(len(L)):
        if L[i]!=T[i]: c+=1
    return c

def M_dis(L, T):
    c = 0
    for i in range(len(L)):
        d = (L[i][0] - T[i][0])**2 + (L[i][1] - T[i][1])**2
        c += d
    return c

def plotout(L, size):
    c = [[0 for i in range(size)] for j in range(size)]
    for i in range(len(L)):
        x, y = L[i]
        c[x][y] = i
    print('<')
    for i in c:
        print(i)
    print('>')
    # return c


def puzzle_solver(filename):
    file = np.loadtxt("/Users/colinwan/Desktop/Coursera_algo/Python/Week 4/8puzzle/" + filename + ".txt", skiprows=1)
    size = int(
        np.loadtxt("/Users/colinwan/Desktop/Coursera_algo/Python/Week 4/8puzzle/" + filename + ".txt", usecols=(0))[0])

    T = [(size-1, size-1)]
    for i in range(size):
        for j in range(size):
            T.append((i, j))
    T.pop(-1)
    L = [None]*size**2
    for i in range(size):
        for j in range(size):
            L[int(file[i][j])] = (i, j)

    closed_list = [L]
    PQ = [None, (H_dis(L, T), L)]
    k=0
    c = 2
    max_len = math.factorial(size**2)
    while H_dis(L, T)>0 and k<1000000:
        L = PQ.pop(1)[1]
        if L not in closed_list: closed_list.append(L)
        neighbors = []
        if L[0][0] > 0: neighbors.append(L.index((L[0][0]-1, L[0][1])))
        if L[0][0]<size-1: neighbors.append(L.index((L[0][0]+1, L[0][1])))
        if L[0][1]>0: neighbors.append(L.index((L[0][0], L[0][1]-1)))
        if L[0][1]<size-1: neighbors.append(L.index((L[0][0], L[0][1]+1)))

        for ind in neighbors:
            temp = L.copy()
            temp[0], temp[ind] = L[ind], L[0]
            d = H_dis(temp, T)
            if (d, temp) not in PQ and temp not in closed_list:
                PQ.append((d, temp))
                swim(PQ, len(PQ) - 1)

        if len(closed_list) == max_len:
            print('This is not solvable')
            break

        if PQ[1][0] == 0:
            print('Solved ' + filename)
            break

        if L == PQ[1][1]:
            L = PQ[c][1]
            c += 1
        else:
            L = PQ[1][1]
            c = 2

        k+=1

    print('not working') if k == 1000000 else print('this took '+str(k)+' iterations')

# for i in range(10,51):
filename = 'puzzle' + str(50)

puzzle_solver(filename)