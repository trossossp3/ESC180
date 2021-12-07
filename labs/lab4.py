import math

def count_evens(L):
    num = 0
    for i in L:
        if(i%2==0):
            num+=1
    return num
def list_to_string(Lis):
    s1=""
    for i in Lis:
        s1+=str(i)+", "
    return s1

def simplify_fraction(n,d):
    n1 = min(n,d)
    div=0
    for i in range(n1,0,-1):
        if n%i==0 and d%i==0:
            div = i
            break
    if(div>0):
        return (n/div,d/div)
    else:
        return (n,d)
    # return n,d if div==0 else n/div,d/div

def leibniz(closeness):
    pi =0
    isClose = False
    x=0
    while(not isClose):
        pi += ((-1)**x)/(2*x+1)
        x+=1
        if(int(math.pi*10**closeness) == int(pi*4*10**closeness)):
            return pi*4
    

if __name__ == "__main__":
    print(simplify_fraction(18,9))
    print(leibniz(3))
    # print(count_evens({1,2,3,4,6}))
    # print(list_to_string({1,2,3,4,5,6}))
    