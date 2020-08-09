import datetime
import random

def selection_sort(L):
    L=L.copy()
    for i in range(len(L)):
        min_index = L.index(min(L[i:]))
        L[i], L[min_index] = L[min_index], L[i]
    return L

def insertion_sort(L, h=1):
    L=L.copy()
    for i in range(len(L)):
        j = i
        while j>=h and L[j]<L[j-h]:
            L[j], L[j-h] = L[j-h], L[j]
            j-=1
    return L

def shell_sort(L):
    L=L.copy()
    x = (len(L)-1)//3+1
    for i in range(x, -1, -1):
        L = insertion_sort(L, 3*i+1)
    return L

def merge_sort(L):
    L=L.copy()
    if len(L)==1:
        return L
    m = len(L)//2
    first = merge_sort(L[:m])
    second = merge_sort(L[m:])
    r = []
    i, j = 0, 0
    while i<len(first) or j<len(second):
        if first[i]<=second[j]:
            r.append(first[i])
            i+=1
        else:
            r.append(second[j])
            j+=1
        if i == len(first):
            r.extend(second[j:])
            j = len(second)
        if j == len(second):
            r.extend(first[i:])
            i = len(first)
    return r


def quick_sort(L, start, end):

    if start>=end:
        return
    p = random.randrange(start, end)
    L[p], L[start] = L[start], L[p]
    c = start
    i = start+1
    j = end

    while i<=j:
        if L[i] < L[c]:
            L[c + 1:i + 1], L[c] = L[c:i], L[i]
            c+=1
            i+=1
        elif L[i] > L[c]:
            L[i], L[j] = L[j], L[i]
            j-=1
        elif L[i] == L[c]:
            i+=1

    quick_sort(L, start, c)
    quick_sort(L, i, end)


L = [3,1,2,5,1,3,1,5,6,2,4]
quick_sort(L, 0, len(L)-1)











# L = random.sample(range(1, 1000), 100)
# print(L)
#
# t1_1 = datetime.datetime.now()
# L1=selection_sort(L)
# print(L1)
# t2_1 = datetime.datetime.now()
# print(t2_1-t1_1)
#
# t1_2 = datetime.datetime.now()
# L2 = insertion_sort(L)
# print(L2)
# t2_2 = datetime.datetime.now()
# print(t2_2-t1_2)
#
# t1_3 = datetime.datetime.now()
# L3 = shell_sort(L)
# print(L3)
# t2_3 = datetime.datetime.now()
# print(t2_3-t1_3)
#
# t1_4 = datetime.datetime.now()
# L4 = merge_sort(L)
# print(L4)
# t2_4 = datetime.datetime.now()
# print(t2_4-t1_4)
#
# L.sort()
# print(L1==L2==L3==L)