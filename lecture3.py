#type: int, float, str, bool

print(int(3.14)) #cast float to int

print(float(3)) #cast int to float

print(str(3.14)) #cast float to str
approx_pi = 3.14

s1="The value of Pi is approx: " + str(approx_pi)

# "abc"+5 #doest work

# int("3.14") #doest work

print(int(float("3.14")))

s1="abc"
if s1:
    print("s1 isnt empty")

a= 0
if a:
    print("a is not empty")

print("hello")

def adjust_grade():
    global grade
    grade = grade-5
    print("new grade in funcion"+grade)

if __name__ == '__main__':
    grade = 95
    adjust_grade()
    print("adjusted grade"+adjust_grade)

#proper way to communicate values
def f(a1,b1,c1):
    ...
    ...

    return val
if __name__ == '__main__':
    res = f(1,2,3)