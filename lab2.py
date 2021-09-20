def init():
    global current_value, prev_value
    current_value = 0
    prev_value =0

def display_current_value():
    print("Current value:", current_value)


def add(to_add):
    global current_value, prev_value
    prev_value = current_value
    current_value += to_add


def mutliply(to_multiply):
    global current_value, prev_value
    prev_value = current_value
    current_value *= to_multiply


def divide(to_divide):
    if(to_divide == 0):
        print("cant divide by 0")
        return
    global current_value, prev_value
    prev_value = current_value
    current_value /= to_divide


def save():
    global temp
    temp = current_value
    print("value: " + str(temp) + " saved to memory")


def recall():
    global current_value, temp
    current_value = temp
    print("saved value: "+str(temp)+" set to current value")

def undo():
    global current_value, prev_value
    current_value, prev_value = prev_value, current_value

if __name__ == "__main__":
    current_value = 0
    prev_value =0
    display_current_value()
    add(5)
    display_current_value()
    undo()
    display_current_value()
    mutliply(2)
    display_current_value()
    divide(12)
    display_current_value()
    save()
    add(12)
    display_current_value()
    recall()
    display_current_value()
    add(5)
    save()
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()
  


