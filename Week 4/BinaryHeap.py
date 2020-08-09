import random

def swim(L, ind):
    c = L[ind]
    # ind = ind//2
    while ind >= 2 and L[ind//2] <= c:
        print(L[ind], c)
        L[ind], L[ind//2] = L[ind//2], L[ind]
        ind = ind//2
        print(L, ind)

def sink(L, ind, end=None):

    # print('Sinking')
    c = L[ind]
    ind = ind * 2 + 1 if ind * 2 + 1 < len(L[:end]) and L[ind * 2] < L[ind * 2 + 1] else ind * 2
    # print(ind)
    while ind < len(L[:end]) and L[ind] >= c:
        # print(L[ind], c)
        L[ind], L[ind//2] = L[ind//2], L[ind]
        ind = ind * 2 + 1 if ind * 2 + 1 < len(L[:end]) and L[ind * 2] < L[ind * 2 + 1] else ind * 2
        # print(L, ind)
    # print('sunk')

def heaporder(L):
    for i in range(len(L)-1, 1, -2):
        # print(L[i], i//2)
        sink(L, i//2)
        # print(L)

# def heapinsert(L, x):


def heapsort(L):
    L.insert(0,None)
    heaporder(L)
    # print("ordered")
    # print(L)
    i = len(L)-1
    while len(L)>2 and i>1:
        # print(L[i], i)
        L[1], L[i] = L[i], L[1]
        # print(L[:i])
        sink(L, 1, i)
        i-=1
        # print(L)
    L.pop(0)


L = random.sample(range(0, 100), 100)
T = list(range(100))
c= 0
L_list = []
L_false_list = []
for i in range(50):
    L = random.sample(range(0, 100), 100)
    t = L.copy()
    heapsort(L)
    if L!=T:
        c+=1
        L_list.append(t)
        L_false_list.append(L)

for i in range(len(L_list)):
    print(L_false_list[i])
print(c)
