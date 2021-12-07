def selection(L):

    for i in range(len(L)-1):
        maxind = max_i(L, len(L)-1-i)
        L[maxind], L[-1-i] =  L[-1-i], L[maxind]
    print(L)

def max_i(L,end):
    index = 0
    max = 0
    for i in range(1,end+1):
        if L[i] >max:
            max = L[i]
            index = i
    return index
selection([1,6,3,4])