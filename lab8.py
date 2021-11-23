import numpy as np


def print_matrix(M_lol):
    arr = np.array(M_lol)
    print(arr)

def get_lead_ind(row):
    for i in range(row):
        if (row[i] != 0):
            return i, row[i]
    return len(row)

def get_row_to_swap(M, start_i):
    leadIndex = []
    for i in range(start_i, len(M)):
        leadIndex[i] = get_lead_ind(M[i])
    return(np.argmin(leadIndex))

def add_rows_coeffs(r1,c1,r2,c2):
    x1 = np.multiply(r1,c1)
    x2 = np.multiply(r2,c2)
    return np.add(x1,x2)

def eliminate(M, row_to_sub, best_lead_ind):
    row_sub = M[row_to_sub]
    coefs = []
    for i in range(best_lead_ind, len(M)):
        coefs.append(get_lead_ind(M(i))[1])
        M[i] = add_rows_coeffs(M[row_to_sub],-1*get_lead_ind(M(i))[1],M[i],1)

def forward_step(M):
    for i in range(len(M)):
        row_to_swap = get_row_to_swap(M, i)
        lead_ind = get_lead_ind(M[row_to_swap])
        if(row_to_swap > i): 
           
            # Do the swapping
            M[row_to_swap], M[i] = M[i], M[row_to_swap]
        eliminate(M,i,lead_ind)

def backward_step(M):
    for i in range(len(M)):
        row = len(M) - i-1
        lead_ind = get_lead_ind(M[row])
        
        inverted = M[::-1]
        eliminate(inverted, i, lead_ind)
        M = inverted[::-1]

    for i in range(len(M)):
        lead_ind = get_lead_ind(M[i])
        if(lead_ind < len(M[i])):
            lead_coefficient = M[i][lead_ind]
            M[i] = add_rows_coeffs(M[i], 1/lead_ind, M[i],0)
    return M

    
def numpy_confirm(M, x):
    M = np.array(M)
    x = np.array(x)
    b = (np.matmul(M,x)).tolist()
    return b

def guassian_elimination(M, b):
    init_m = M.copy()
    augmented = M.copy()
    for i in len(augmented):
        augmented[i].append(b[i])

    augmented = forward_step(augmented)
    augmented = backward_step(augmented)

    rank = 0
    solutions = True
    x = []
    for row in augmented:
        x.append(row[-1])
        ind = get_lead_ind(row)
        if(ind == len(row)-1): 
            has_solutions = False
        elif(ind < len(row)-1): 
            rank += 1
    if(not has_solutions):
        print("This system has no solutions")
        return
    
    # Analyze rank for types of solutions
    cols = len(init_m[0])
    if(rank < cols): 
        print("This system has infinite solutions")
        return
    
    print("algorithm found solution of " + x)
    print("numpy library found " + numpy_confirm(init_m, x))