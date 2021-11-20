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

