# import lab2

def sum_cubes(n):
    total =0
    for x in range(1,n+1):
        total+=x**3
    return(total)

def sum_cubes_formula(n):
    return((n**2*(n+1)**2)/4)

def check_sum(n):
     return (sum_cubes_formula(n) == sum_cubes(n))
def check_sums_up_to_n(N):
    
    for x in range(1, N):
        if (sum_cubes_formula(x) != sum_cubes(x)):
            return
    return True
def leibniz(n):
    pi =0
    for x in range(0,n):
        pi += ((-1)**x)/(2*x+1)
    return pi*4
if __name__ == "__main__":
    # lab2.init()
    # print(lab2.current_value)
    # lab2.add(3)
    # print(lab2.current_value)
    # print(check_sum(1000))
    # print(sum_cubes(100000))
    # print(sum_cubes_formula(100000))
    # print(check_sums_up_to_n(100000))
    print(leibniz(1000000000))

