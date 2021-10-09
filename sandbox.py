class Person():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def print_name(self):
        print(self.fname + self.lname)

x= Person("t", "r")
x.print_name()

    
class Child(Person):
    def __init__(self,fname,lname, age):
        super().__init__(fname, lname)
        self.age = age
    
    def get_age(self):
        print(self.age)
y=Child("c", "a", 12)
y.print_name()
y.get_age()
