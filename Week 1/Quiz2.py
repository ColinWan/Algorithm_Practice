def bsearch(L, x):
    # print(L)
    if not L:
        return [-1, False]
    m = len(L)//2
    if L[m]==x:
        return [m, True]
    else:
        [temp, b] = bsearch(L[m+1:], x) if L[m]<x else bsearch(L[:m], x)
        temp = temp + m +1 if b and L[m]<x else temp
        return [temp, b] if b else [-1, b]

def tsum(L):
    result = []
    for i in range(len(L)):
        # print('Current i', L[i])
        aim = -L[i]

        for j in range(len(L[i+1:])):
            # print('Current j', L[j+i+1])
            target = aim - L[j+i+1]
            # print('target', target)
            l = L[i+2+j:].copy()
            # print('l1', l, target)

            [ind, b] = bsearch(l, target)
            # if b:
            #     print('ind', ind, l[ind])
            if b:
                # print('added', [L[i], L[i+j+1], l[ind]])
                result.append([L[i], L[i+j+1], l[ind]])
    return result

L = [-7,-3,-2,-1,0,1,2,3,4,5]
result = tsum(L)
print(result)