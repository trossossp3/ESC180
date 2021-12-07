# Problem 1

def list1_starts_with_list2(list1, list2):
    if(len(list1) < len(list2)):
        return False
    temp = [0]*len(list2)
    for i in range(0, len(list2)):
        temp[i]=list1[i]
    return temp == list2
print(list1_starts_with_list2([1,2,3,4,5], [1,2,3,4,5,6]))
# Problem 2
arr1 =[6,7,8]
arr2 =[1,2,3,4,5,6,7,8]
def function(arr1, arr2):
    x = (len(arr2))-(len(arr1))
    for i in range (0, x+1):
        y =arr2[i:i+len(arr1)]
        if (y == arr1):
            return True
    return False
print(function(arr1,arr2))

# PROBLEM 3
list0 = [1,2,2,3,4,5]
def repeats(list0):
    for i in range(1, len(list0)):
        if list0[i] == list0[i-1]:
            return True
    return False

print(repeats(list0))
# Porblem 4

def print_matrix_dim(M):
    x = len(M)
    y = len(M[0])
    return str(x)+"x"+str(y), x, y

print(print_matrix_dim([[1,2],[3,4],[5,6] ])[0])

def mult_M_v(M, v):
   
    rows = print_matrix_dim(M)[1]
    cols = print_matrix_dim(M)[2]
    vector = [0]*rows

    for i in range(0, rows):
        for j in range(0, cols):
            vector[i]+=M[i][j] * v[j]

    print(vector)

M = [[10,20,30],
    [40,50,60]]
V = [10,20,30]

mult_M_v(M, V)


