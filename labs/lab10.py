#question 1
def power(x,n):
    if n ==1:
        return x
    return x*power(x,n-1)
    
#question 2
print(power(3,3))
L1 = [1,3,5,7]
L2 = [2,4,6,8]

def interleave(L1, L2):
    intleave = L1 + L2
    intleave[::2] = L1
    intleave[1::2] = L2
    print("Interleaved List: " + str(intleave))

interleave(L1, L2)


#question 3
def reverse_rec(L):
    if len(L) == 0:
       return []
    return([L[len(L)-1]] + reverse_rec(L[:len(L)-1]))
print(reverse_rec([1,2,3,4,5,6]))

#problem 4
def zigzag1(L):
    if len(L) == 0:
        print('')
    elif len(L) == 1:
        print(L[len(L) // 2], end = " ")
    else:
        print(L[len(L)//2],L[len(L)//2 - 1], end = " ")
        zigzag1(L[0:len(L)//2 - 1] + L[len(L)//2 + 1:])

L = [1,2,4,6,7,8]
zigzag1(L)


#question 5
def is_balanced(s):
    #find the first closing bracket
    #find the last opening bracket in substring upto first closing bracket
    #do it again exluding pair
    # print(s)
    close = s.find(')') 
    # print(s[:close])
    if close == -1:
        return '(' not in s
    

    start = s[:close].rfind('(')
  
    if start == -1:
        return False 
       
    s2 = s[:start] + s[close+1:]
    return is_balanced(s2)

print(is_balanced("(a(a)sa)aa())"))