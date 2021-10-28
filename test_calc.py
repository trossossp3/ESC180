def init():
    global x
    x=10

def y(b=x):
    print(b)
if __name__ == "__main__":
    init()
    print(x)
